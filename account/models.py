from typing import Optional
from tortoise import models, fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from pydantic import BaseModel
import bcrypt


class User(models.Model):
    id = fields.IntField(pk=True)
    display_name = fields.CharField(max_length=128, null=False)
    email = fields.CharField(max_length=128, unique=True, null=False)
    password = fields.CharField(max_length=256, null=True)
    is_active = fields.BooleanField(default=True, null=False)

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt(),
        ).decode()

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode(), self.password.encode())


User_Pydantic = pydantic_model_creator(User, name='User')


class UserCreate(BaseModel):
    display_name: str
    email: str
    password: str


class UserRead(BaseModel):
    id: int
    email: str
    display_name: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
