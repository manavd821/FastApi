from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status 
from sqlalchemy import select
from app.db.config import DbSession
from app.account.utils import decode_token
from app.account.tables import users as user_table
from app.account.schemas import User

oauth2_schema = OAuth2PasswordBearer(tokenUrl="account/login")

async def get_current_user(session : DbSession, token :str = Depends(oauth2_schema)): 
    payload = decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credential"
        )
    stmt = select(user_table).where(user_table.c.user_id == int(payload.get("sub")))
    user = (await session.execute(stmt)).mappings().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User Not Found")
    return user

async def require_admin(user : User = Depends(get_current_user)):
    if not user["is_admin"]:
        raise HTTPException(403, "You are not admin")
    return user