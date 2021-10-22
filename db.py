from dotenv import load_dotenv
from sqlmodel import Session, create_engine
import os
load_dotenv()

engine = create_engine(os.environ.get('DB_URL', 'db.sqlite'))
session = Session(engine)
