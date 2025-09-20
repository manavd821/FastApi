from app.db.config import sessionLocal
from sqlalchemy import select
from app.user.models import User

async def insert_user(name : str, email : str):
    async with sessionLocal() as session:
        user = User(name = name, email = email)
        session.add(user)
        await session.commit()
        
async def get_all_users():
    async with sessionLocal() as session:
        stmt = select(User)
        users = await session.scalars(stmt)
        return users.all()     

