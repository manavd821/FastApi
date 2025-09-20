from app.db.config import sessionLocal
from app.user.models import User
from sqlalchemy import select

# insert user
def insert_user(name: str, email : str):
    with sessionLocal() as session:
        user = User(name = name, email = email)
        session.add(user)
        session.commit()

# read all user
def get_all_user():
    with sessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt)
        return users.all()