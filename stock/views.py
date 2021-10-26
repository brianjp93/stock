import settings
from typing import Optional

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db import get_session
from account.models import User
from account.utils import get_current_active_user
import finnhub


client = finnhub.Client(api_key=settings.FINNHUB_KEY)


router = APIRouter(
    prefix="/stock",
    tags=["stock"],
)


@router.get('/basic/{symbol}/')
async def basic_financials(symbol: str):
    response = client.company_basic_financials(symbol, 'all')
    return response


@router.get('/search/')
async def search(q: str):
    response = client.symbol_lookup(q)
    return response
