from fastapi import APIRouter, Depends, HTTPException, status, Request, Query
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from app.account.services import create_user, authentic_user, create_refresh_token_in_table, process_email_verification,verify_email_token, change_password,process_password_reset,reset_password_with_token
from app.account.schemas import UserCreate, User
from app.account.utils import verify_refresh_token,revoke_refresh_token
from app.db.config import DbSession
from app.account.dependencies import get_current_user, require_admin
from typing import Annotated
router = APIRouter(prefix='/account', tags=["Account"])

@router.post("/register")
async def register_user(session : DbSession, user : UserCreate):
    return await create_user(session, user)

@router.post('/login')
async def login(session : DbSession, form_data : OAuth2PasswordRequestForm = Depends()):
    user = await authentic_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credential"
        )
    tokens = await create_refresh_token_in_table(session=session, user=user)
    response = JSONResponse(
        content= {"access_token" : tokens["access_token"]},
        status_code=status.HTTP_202_ACCEPTED,
    )
    response.set_cookie(key="refresh_token", value=tokens["refresh_token"], httponly=True, secure=True, samesite="lax", max_age= 7 * 24 * 60 *60)
    return response

@router.post('/refresh')
async def refresh_token(session : DbSession, request : Request):
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Refresh token missing" 
        )
    user = await verify_refresh_token(session=session, token=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Refresh token invalid or expired" 
        )
    return await create_refresh_token_in_table(session=session, user=user)

@router.get('/me')
async def get_user(user = Depends(get_current_user)):
    return user

@router.post("/verify-request")
async def send_verification_email(user = Depends(get_current_user)):
    return process_email_verification(user)

@router.get('/verify')
async def verify_email(session : DbSession, token : Annotated[str, Query()]):
    return await verify_email_token(session, token)
    
@router.post("/change-password")
async def password_change( *, session : DbSession, user = Depends(get_current_user) , new_password : str):
    await change_password(session, user, new_password)
    return {"msg" : "changed password successfully"}

@router.post("/forgot-password")
async def forgot_password(session : DbSession, email :str):
    return await process_password_reset(session,email)

@router.get('/reset-password')
async def reset_password(session : DbSession, token : str, new_password : str):
    return await reset_password_with_token(session, token, new_password)

@router.get("/admin")
async def get_admin(admin  = Depends(require_admin)):
    return {"msg" : f"Welcome admin {admin['name']}"}

@router.post("/logout")
async def logout(session : DbSession, request : Request): 
    token = request.cookies.get("refresh_token", None)
    if token:
        await revoke_refresh_token(session, token)
        
    response = JSONResponse(
       content = {"detail" : "Logged out"}
    )
    response.delete_cookie("refresh_token")
    return response