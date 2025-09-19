from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

URL = 'sqlite:///mydb.db'

engine = create_engine(url=URL,echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)