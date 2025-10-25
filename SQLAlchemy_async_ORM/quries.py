from model import User
from db import asych_session
from sqlalchemy import select

async def insert_user(name : str, email : str):
    async with asych_session() as session:
        user = User(name=  name, email = email)
        session.add(user)
        await session.commit()
        
async def get_user_by_id(id : int):
    async with asych_session() as session:
        stmt = select(User).where(User.id == id)
        result = await session.execute(stmt)
        return result.one_or_none()