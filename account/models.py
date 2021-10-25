from typing import Optional
from sqlmodel import SQLModel, Field, Column, String
import bcrypt
import settings


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    display_name: str
    email: str = Field(sa_column=Column('email', String(320), unique=True, nullable=False, index=True))
    password: str
    is_active: bool = True

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(
            password.encode(),
            settings.SECRET.encode(),
        ).decode()

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode(), self.password.encode())


class UserCreate(SQLModel):
    display_name: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    email: str
    display_name: str
