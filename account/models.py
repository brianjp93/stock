from sqlmodel import SQLModel, Field, Column
import bcrypt
import settings
from db import session

class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    display_name: str
    email: str = Field(sa_column=Column(unique=True))
    password: str

    def set_password(self, password: str):
        self.password = str(bcrypt.hashpw(
            password.encode(),
            settings.SECRET.encode(),
        ))
        session.add(self)

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode(), self.password.encode())
