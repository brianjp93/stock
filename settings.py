import os
from dotenv import load_dotenv
load_dotenv()

SECRET: str = os.getenv('SECRET', '')
assert SECRET
DB_URL: str = os.getenv('DB_URL', 'db.sqlite')
FINNHUB_KEY: str = os.getenv('FINNHUB_KEY', '')
assert FINNHUB_KEY
