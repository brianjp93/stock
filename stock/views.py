from config.settings import get_settings
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from account.utils import get_current_active_user
from stock.models import (
    Ticker, Ticker_Pydantic, Transaction, TransactionCreate,
    Transaction_Pydantic,
)
import finnhub


settings = get_settings()
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
async def search(q: str):
    response = client.symbol_lookup(q)
    ticker_list = []
    symbols = {item['symbol'] for item in response.get('result', [])}
    qs = await Ticker.filter(code__in=symbols).values('code')
    codes = {x['code'] for x in qs}
    for item in response.get("result", []):
        if item['symbol'] not in codes:
            ticker = Ticker(name=item["description"], code=item["symbol"])
            ticker_list.append(ticker)
    if ticker_list:
        await Ticker.bulk_create(ticker_list)
    return response


@router.get("/tickers/", response_model=List[Ticker_Pydantic])
async def tickers(page: int = 1, limit: int = 100):
    if 0 > limit > 100:
        raise HTTPException(400, "limit must be between 1 and 100")
    end = page * limit
    start = end - limit
    qs = Ticker.all().order_by('code').limit(limit).offset(start)
    return qs


@router.post("/transactions/", response_model=Transaction_Pydantic)
async def create_transaction(
    *,
    user = Depends(get_current_active_user),
    transaction_create: TransactionCreate,
):
    user = await user
    qs = Ticker.filter(code__icontains=transaction_create.symbol)
    if ticker := await qs.first():
        transaction_create.user_id = user.id
        transaction_create.ticker_id = ticker.id
        transaction = Transaction(**transaction_create.dict())
        await transaction.save()
        return transaction
    raise HTTPException(404, 'Symbol could not be found.')
