from typing import Optional
from tortoise import fields, models
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class Ticker(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=256)
    code = fields.CharField(max_length=64, unique=True)

Ticker_Pydantic = pydantic_model_creator(Ticker, name='Ticker')
TickerIn_Pydantic = pydantic_model_creator(Ticker, name='TickerIn', exclude_readonly=True)

class Transaction(models.Model):
    id = fields.IntField(pk=True)
    ticker = fields.ForeignKeyField('models.Ticker', on_delete=fields.CASCADE)
    user = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE)
    count = fields.DecimalField(16, 4)
    cost = fields.DecimalField(16, 2)
    created_at = fields.DatetimeField(auto_now_add=True)

Transaction_Pydantic = pydantic_model_creator(Transaction, name='Transaction')

class TransactionCreate(BaseModel):
    symbol: str
    count: float
    cost: Decimal
    created_at: datetime
    user_id: Optional[int]
    ticker_id: Optional[int]
