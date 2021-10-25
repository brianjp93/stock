from sqlmodel import SQLModel, Field, Column, String, Relationship, Float
from account.models import User
from decimal import Decimal
from typing import Optional


class Ticker(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    code: str = Field(sa_column=Column('code', String(10), unique=True))


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
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
