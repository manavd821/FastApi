from app.db.config import DbSession
from fastapi import APIRouter, Request, Form, Depends, Header
from fastapi.responses import JSONResponse
from app.account.services import authenticate_user
from app.account.utils import create_refresh_token,decode_token
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Annotated


class LoginRequest(BaseModel):
    email: str
    password: str

router = APIRouter(prefix="/resource", tags = ["resources"])

# make dependencies to verify user before allocating resource
def get_current_user(request : Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401,detail="Token not found")
    print(token)
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401,detail="Token is not valid")
    return payload
    
def get_current_user_method2(authorization: Annotated[str, Header()]):
    schema, token = authorization.split()
    if schema.lower() != 'bearer':
        raise HTTPException(status_code=401,detail="Schema not matched")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401,detail="Token is not valid")
    return payload
    
        

@router.post('/login-hs256')
async def login(session: DbSession, request: Request ,data : LoginRequest):
    user = await authenticate_user(session,data.email, data.password)
    # generate refresh token
    payload = {
        "sub" : str(user['user_id']),
        "name" : user["name"]
    }
    token =await create_refresh_token(session, user , payload)
    response = JSONResponse(
        content= {
            "msg" : "login successfull",
            "access_token" : token["access_token"]
        },
        status_code=200
    )
    response.set_cookie("access_token", token["access_token"],max_age=15 * 60 ,secure=True,samesite="lax", httponly=True)
    return response
    
@router.get("/{resource_name}")
async def get_resource(resource_name: str, user=Depends(get_current_user)):
    return {"resource": resource_name, "user": user}
