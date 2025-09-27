from app.account.tables import users as user_table, refresh_tokens as refresh_token_table
from app.db.config import DbSession
from app.account.schemas import UserCreate, User
from app.account.utils import hash_passoword, verify_password
from sqlalchemy import select, insert, update
from fastapi import HTTPException, status
from app.account.utils import create_refresh_token, create_email_verification_token, verify_token_and_get_user_id, get_user_by_email, create_password_reset_token

async def create_user(session : DbSession, user : UserCreate):
    stmt = select(user_table).where(user_table.c.email == user.email)
    existing_email = await session.execute(stmt)
    if existing_email.first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists!!"
        )
    new_user_stmt = insert(user_table).values(
        # {
        #     "email" : user.email,
        #     "hashed_password" : user.hashed_password,
        #     "name" : user.name,
        #     "is_verified" : False
        #  }
        # or
        email=user.email,
        hashed_password=hash_passoword(user.password),
        name=user.name,
        is_verified=False,
        is_admin = user.is_admin,
        is_active = user.is_active
    ).returning(user_table.c.user_id)
    result = await session.execute(new_user_stmt)
    await session.commit()
    
    new_user_id = result.scalar()
    return new_user_id
    
async def authentic_user(session : DbSession, email : str, password : str):
    stmt = select(user_table).where(user_table.c.email == email)
    result = await session.execute(stmt)
    user = result.mappings().first() #Fetch the first row or None if no row is present.
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

async def create_refresh_token_in_table(session : DbSession, user : User):
    data = create_refresh_token(user=user)
    stmt = insert(refresh_token_table).values(
        user_id = data["user_id"],
        token = data["token"],
        expires_at = data["expires_at"]
    )
    await session.execute(stmt)
    await session.commit()
    return {
        "access_token" : data["access_token"],
        "refresh_token" : data["token"],
        "token_type" : "bearer"
    }
    
def process_email_verification(user : User):
    token = create_email_verification_token(user.user_id)
    link = f"http://localhost:8000/account/verify?token={token}"
    print(f"verify your email : {link}")
    return {"msg" : "verification email sent"}

async def verify_email_token(session : DbSession, token : str):
    user_id  = verify_token_and_get_user_id(token, "verify") 
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expire token"
        )
    stmt = (
        update(user_table).
        values(is_verified = True).
        where(
                user_table.c.user_id == user_id,
                user_table.c.is_verified == False
            ).
        returning(user_table.c.user_id)
    )
    result = await session.execute(stmt)
    await session.commit()
    updated_user = result.first()
    if not updated_user:
        # No rows updated → user not found
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"msg" : "Email verified successfully"}

async def change_password(session : DbSession, user , new_password : str):
    stmt = update(user_table).values(
        hashed_password = hash_passoword(new_password)
    ).where(
        user_table.c.user_id == user["user_id"],
        user_table.c.hashed_password != hash_passoword(new_password)
    )
    await session.execute(stmt)
    await session.commit()
    
async def process_password_reset(session : DbSession, email : str):
    user : User = await get_user_by_email(session, email)
    if not user:
        raise HTTPException(detail="User not found",status_code= 403)
    token = create_password_reset_token(user.user_id)
    link = f"http://localhost:8000/account/reset-password?token={token}"
    print(f"Reset your password: {link}")
    return {"msg" : "Password reset link set"}
    
async def reset_password_with_token(session : DbSession, token : str, new_password : str):
    user_id = verify_token_and_get_user_id(token, "reset")
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expire token"
        )
    stmt = select(user_table).where(user_table.c.user_id == user_id)
    user = (await session.execute(stmt)).mappings().first()
    await change_password(session, user,new_password)
    return {"msg" : "Password reset successful"}