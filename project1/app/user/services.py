from app.user.models import User, Address
from app.db.config import SessionLocal
from sqlalchemy import select

async def insert_user(name : str, email : str):
    async with SessionLocal() as session:
        user = User(name= name, email = email)
        session.add(user)
        await session.commit()

async def insert_address(street : str, city : str, state : str, user_id : int):
    async with SessionLocal() as session:
        user_address = Address(street = street, city = city, state = state, id = user_id)
        session.add(user_address)
        await session.commit()
        
async def get_all_user():
    async with SessionLocal() as session:
        stmt = select(User)
        users = await session.scalars(statement=stmt)
        users = users.all()
        return users
    
async def get_all_address():
    async with SessionLocal() as session:
        stmt = select(Address)
        user_address = await session.scalars(statement=stmt)
        user_address = user_address.all()
        return user_address