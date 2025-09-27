from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from decouple import config
from app.db.config import DbSession
from app.account.schemas import User
from app.account.tables import refresh_tokens as refresh_token_table, users as user_table
from sqlalchemy import select, update
import uuid
from fastapi import HTTPException

SECRET_KEY  = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
pwd_context = CryptContext(
    schemes= ["argon2"],
    deprecated = "auto"
)

def hash_passoword(password : str):
    return pwd_context.hash(password)

def verify_password(plain_pass, hash_pass):
    return pwd_context.verify(plain_pass,hash_pass)

def create_access_token(data : dict, expires_delta : timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp" : expire})
    return jwt.encode(claims=to_encode, key = SECRET_KEY, algorithm = ALGORITHM)

def create_refresh_token(user : User):
    access_token = create_access_token(data={"sub":str(user.user_id)})
    refresh_token_str = str(uuid.uuid4())
    expire_date = datetime.now(timezone.utc) + timedelta(days=7)
    return {
        "access_token" : access_token,
        "user_id" : user.user_id,
        "token" : refresh_token_str,
        "expires_at" : expire_date
    }
    
async def verify_refresh_token(session : DbSession, token : str):
    stmt = select(refresh_token_table).where(refresh_token_table.c.token == token)
    db_token = (await session.execute(stmt)).mappings().first()
    if db_token and not db_token["revoked"]: # refresh token not match with db
        expires_at = db_token["expires_at"]
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo = timezone.utc)
        if expires_at > datetime.now(timezone.utc):
            stmt = select(user_table).where(user_table.c.user_id == db_token["user_id"])
            return (await session.execute(stmt)).mappings().first()
    return None

def decode_token(token : str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        return None
    
def create_email_verification_token(user_id : int):
    expire = datetime.now(timezone.utc) + timedelta(hours=1)
    to_encode = {"sub" : str(user_id), "type" : "verify", "exp" : expire}
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def verify_token_and_get_user_id(token : str, token_type : str):
    try:
        payload = decode_token(token)
        if not payload or payload.get("type") != token_type:
            return None
        return int(payload.get("sub"))
    except JWTError: 
        return None

async def get_user_by_email(session : DbSession, email : str):
    stmt = select(user_table).where(user_table.c.email == email)
    return (await session.execute(stmt)).mappings().first()

def create_password_reset_token(user_id : int):
    expire = datetime.now(timezone.utc) + timedelta(hours=1)
    to_encode = {"sub" : str(user_id), "type" : "reset", "exp" : expire}
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

async def revoke_refresh_token(session : DbSession, token : str):
    stmt = update(refresh_token_table).values(
        revoked = True
    ).where(
        refresh_token_table.c.token == token
    ).returning(
        refresh_token_table.c.refresh_token_id
    )
    result = await session.execute(stmt)
    await session.commit()
    updated_user = result.mappings().first()
    if not updated_user:
        # No rows updated → user not found
        raise HTTPException(status_code=404, detail="Token not found")
    
    print(updated_user)