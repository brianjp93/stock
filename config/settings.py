from dotenv import load_dotenv
from pydantic import BaseSettings
from functools import lru_cache

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str
    APP_NAME = 'Stock'
    DATABASE_URL: str = 'db.sqlite'
    FINNHUB_KEY: str
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    TOKEN_ALGORITHM = 'HS256'
    SMTP_SERVER: str = 'localhost:25'
    MAIL_SENDER = 'noreply@example.com'
    API_PREFIX = '/api'
    HOST = 'localhost'
    PORT = 8000
    BASE_URL = '{}:{}/'.format(HOST, str(PORT))
    MODELS = [
        'account.models',
        'stock.models',
        'aerich.models',
    ]

    class Config:
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    return Settings()
