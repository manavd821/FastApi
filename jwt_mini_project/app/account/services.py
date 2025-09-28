from app.db.config import DbSession
from app.account.tables import users as user_table, refresh_tokens as refresh_token_table
from sqlalchemy import select, insert,update
from fastapi import HTTPException
from app.account.utils import verify_password

async def authenticate_user(session : DbSession ,email : str, password : str):
    stmt = select(user_table).where(user_table.c.email == email)
    user = (await session.execute(stmt)).mappings().first()
    if not user:
        raise HTTPException(401,"User not found.")
    elif not verify_password(password, user["hashed_password"]):
        raise HTTPException(401,"Password not matched.")
    return user
        