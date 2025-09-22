from app.user.models import User, Address
from app.db.config import UserSession
from sqlalchemy import select, update, delete
from app.user.schemas import UserBase
from pydantic import EmailStr

async def insert_user(session : UserSession, user : UserBase):
    try:
        new_user = User(name = user.name, email = user.email)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

    except Exception as e:
        await session.rollback()
        raise e
    
async def read_all_user(session : UserSession):
    try:
        stmt = select(User)
        all_user = (await session.scalars(stmt)).all()
        return all_user
    except Exception as e:
        await session.rollback()
        raise e
        
async def read_user_by_id(session : UserSession, id : int):
    try:
        
        result = await session.execute(select(User).where(User.id == id))
        user = result.scalar_one_or_none()
        return user
    except Exception as e:
        await session.rollback()
        raise e

async def update_user_by_id(session : UserSession, id : int, new_email : EmailStr):
    try:
        stmt = update(User).where(User.id == id).values(email = new_email).execution_options(synchronize_session="fetch")
        await session.execute(stmt)
        await session.commit()
        result = await session.execute(select(User).where(User.id == id))
        user = result.scalar_one_or_none()
        return user
    except Exception as e:
        await session.rollback()
        raise e     

async def delete_user_by_id(session : UserSession, id : int):
    try:
        stmt = delete(User).where(User.id == id)
        result = await session.execute(stmt)
        if result.rowcount == 0:
            # No user was deleted
            return None
        
        await session.commit()
        return id
    except Exception as e:
        await session.rollback()
        raise e    
    