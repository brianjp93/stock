from sqlmodel import SQLModel, Field, Column
import bcrypt
import settings
from db import session

class User(SQLModel, table=True):
    display_name: str
    email: str = Field(sa_column=Column(unique=True))
    password: bytes

    def set_password(self, password: str):
        self.password = bcrypt.hashpw(
            password.encode(),
            settings.SECRET.encode(),
        )
        session.add(self)
