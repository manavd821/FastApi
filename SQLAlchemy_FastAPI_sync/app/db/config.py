from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db_path = os.path.join(BASE_DIR, 'mydb.db')
URL = f"sqlite:///{db_path}"

engine = create_engine(URL, echo = True)
sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)