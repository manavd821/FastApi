from sqlmodel import Session, select
from db import engine
from models import User

def insert_user(name : str, email: str):
    with Session(engine) as session:
        user = User(name = name, email = email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def get_all_user():
    with Session(engine) as session:
        stmt = select(User)
        users = session.exec(stmt)
        return users.all()
    
def get_user_by_id(id : int):
    with Session(engine) as session:
        stmt = select(User).where(User.id == id)
        users = session.exec(stmt)
        return users.one()

