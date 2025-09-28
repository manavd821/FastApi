from jose import JWTError,jwt
from decouple import config
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.db.config import DbSession
from app.account.tables import refresh_tokens as refresh_token_table, users as user_table
from sqlalchemy import select, insert, update
import json
import uuid
from fastapi import HTTPException


SECRET_KEY  = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM", cast = str)
PUBLIC_KEY = config("PUBLIC_KEY")

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated = "auto"
)
def hash_passoword(password : str):
    return pwd_context.hash(password)

def verify_password(plain_pass, hash_pass):
    return pwd_context.verify(plain_pass,hash_pass)

def create_access_token(payload : dict,expires_delta : timedelta = None):
    exp = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    payload.update({"exp" : exp})
    try:
        return jwt.encode(
            claims=payload, key = SECRET_KEY, algorithm = ALGORITHM
            )
    except JWTError:
        print("error bhai")

async def create_refresh_token(session : DbSession, user ,payload : dict):
    access_token = create_access_token(payload, expires_delta=timedelta(minutes=20))
    refresh_token = str(uuid.uuid4())
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    try:
        stmt = insert(refresh_token_table).values(
            user_id = user["user_id"],
            token = refresh_token,
            expires_at = expires_at
        ).returning(refresh_token_table.c.user_id)
        user_id = (await session.execute(stmt))
        await session.commit()
        return {
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "expires_at" : expires_at
        }
    except Exception as e:
        await session.rollback()
        print(f"Bhai Exception: {e}")
        raise HTTPException(
            501,
            "DB Error"
        )
        
def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        print("JWT decode error:", e)
        return None