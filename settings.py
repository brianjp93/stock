import os
from dotenv import load_dotenv
load_dotenv()

SECRET: str = os.getenv('SECRET', '')
assert SECRET
