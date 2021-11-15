from datetime import datetime
from sqlmodel import SQLModel, Field, Column, String, Relationship, Float, TIMESTAMP
from account.models import User
from decimal import Decimal
from typing import Optional


class Ticker(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    code: str = Field(sa_column=Column('code', String(32), unique=True))


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    ticker: Ticker = Relationship()
    ticker_id: int = Field(foreign_key='ticker.id')
    user: User = Relationship()
    user_id: int = Field(foreign_key='user.id')
    count: float
    cost: Decimal = Field(
        sa_column=Column(
            'cost',
            Float(precision=2, asdecimal=True),
            nullable=False,
        )
    )
    created_at: datetime = Field(
        sa_column=Column(
            'created_at',
            TIMESTAMP,
            nullable=False,
        )
    )

class TransactionCreate(SQLModel):
    symbol: str
    count: float
    cost: Decimal
    created_at: datetime
    user_id: Optional[int]
    ticker_id: Optional[int]
