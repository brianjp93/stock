from dotenv import load_dotenv
from sqlmodel import Session, create_engine
import os
load_dotenv()

engine = create_engine(os.environ.get('DB_URL', 'sqlite:///sqlite.db'))

def get_session():
    with Session(engine) as session:
        yield session
