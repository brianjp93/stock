import os
from dotenv import load_dotenv
load_dotenv()

SECRET: str = os.getenv('SECRET', '')
assert SECRET
DB_URL: str = os.getenv('DB_URL', 'db.sqlite')
