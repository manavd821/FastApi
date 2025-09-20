from sqlmodel import create_engine, SQLModel
url = "sqlite:///mydb.db"

engine = create_engine(url=url, echo = True)

def create_tables():
    SQLModel.metadata.create_all(bind = engine)