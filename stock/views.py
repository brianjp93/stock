from datetime import datetime
import settings
from typing import Optional, List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select, func
from db import get_session
from account.models import User
from account.utils import get_current_active_user
from stock.models import Ticker, Transaction, TransactionCreate
import finnhub


client = finnhub.Client(api_key=settings.FINNHUB_KEY)


router = APIRouter(
    prefix="/stock",
    tags=["stock"],
)


@router.get("/basic/{symbol}/")
async def basic_financials(symbol: str):
    response = client.company_basic_financials(symbol, "all")
    return response


@router.get("/search/")
async def search(q: str, session: Session = Depends(get_session)):
    response = client.symbol_lookup(q)
    for item in response.get("result", []):
        query = select(Ticker).where(Ticker.code == item["symbol"])
        if not (ticker := session.exec(query).first()):
            ticker = Ticker(name=item["description"], code=item["symbol"])
            session.add(ticker)
    session.commit()
    return response


@router.get("/tickers/", response_model=List[Ticker])
async def tickers(
    page: int = 1, limit: int = 100, session: Session = Depends(get_session)
):
    if 0 > limit > 100:
        raise HTTPException(400, "limit must be between 1 and 100")
    end = page * limit
    start = end - limit
    query = select(Ticker).order_by(Ticker.code.asc()).limit(limit).offset(start)
    results = session.exec(query).all()
    return results


@router.post("/transactions/", response_model=Transaction)
async def create_transaction(
    *,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_active_user),
    transaction_create: TransactionCreate,
):
    query = select(Ticker).where(Ticker.code.ilike(transaction_create.symbol))
    if ticker := session.exec(query).first():
        transaction_create.user_id = user.id
        transaction_create.ticker_id = ticker.id
        transaction = Transaction.from_orm(transaction_create)
        session.add(transaction)
        session.commit()
        return transaction
    raise HTTPException(404, 'Symbol could not be found.')
