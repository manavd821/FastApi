from db import engine 
from tables import users
from sqlalchemy import insert, update, delete, select

# insert user
async def create_user(name : str, email : str):
    async with engine.connect() as conn:
        stmt = insert(users).values(name = name, email = email)
        await conn.execute(stmt)
        await conn.commit()

# get user by id 
async def get_user_by_id(id : int):
    async with engine.connect() as conn:
        stmt = select(users).where(users.c.id == id)
        result = await conn.execute(stmt)
        return result.first()

# update user email
async def update_user_email(id : int, new_email : str):
    async with engine.connect() as conn:
        stmt = update(users).where(users.c.id == id).values(email = new_email)
        await conn.execute(stmt)
        await conn.commit()