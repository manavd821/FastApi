from fastapi import FastAPI, status, HTTPException, Path, Request
from app.user import services as user_service
from app.user.schemas import UserBase,UserCreate
from typing import Annotated, Union
from app.db.config import UserSession
from pydantic import EmailStr

app = FastAPI()

@app.get('/')
async def home(request : Request):
    if request:
        return {
                    "greet" : "Hello",
                    "Method" : request.method,
                    "headers" : request.headers,
                    "cookie" : request.cookies,
                    "client": request.client,
                    "base_url":request.base_url,
                    "path_params": request.path_params,
                    "query_params":request.query_params,
                    "receive": request.receive,
                    # "user": request.user,
                    "receive": request.receive,
                    # "session": request.session,
                    "state": request.state
                }
    return "Hello Bhai"

# Create 
@app.post('/user', status_code=status.HTTP_201_CREATED)
async def create_user(session : UserSession, user : UserCreate):
    try:
        created_user = await user_service.insert_user(session=session, user=user)
        return {"status" : "Done", "user_id" : created_user.id }, status.HTTP_202_ACCEPTED
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {e}"
        )
# Read all user
@app.get('/users',response_model=list[UserBase],status_code=status.HTTP_202_ACCEPTED)
async def get_all_user(session : UserSession):
    try:
        all_user = await user_service.read_all_user(session=session)
        return all_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
        
# Read user by id
@app.get('/users/{user_id}', response_model=Union[UserBase, str] ,status_code=status.HTTP_202_ACCEPTED)
async def get_user_by_id(session : UserSession, user_id : Annotated[int, Path()]):
    try:
        user = await user_service.read_user_by_id(session=session,id=user_id)
        if user is not None:
            return user
        return "User not Exists"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

# Update
@app.put('/users/{user_id}', response_model=Union[int, str, dict[str, int]] ,status_code=status.HTTP_202_ACCEPTED)
async def update_user_by_id(session : UserSession, user_id : Annotated[int, Path()], new_email : EmailStr):
    try:
        user = await user_service.update_user_by_id(session=session,id=user_id, new_email=new_email)
        if user is not None:
            return {"updated_id" : user.id}
        return "User not Exists"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
# Delete
@app.delete('/users/{user_id}', response_model=Union[int, str, dict[str, int]] ,status_code=status.HTTP_202_ACCEPTED)
async def delete_user_by_id(session : UserSession, user_id : Annotated[int, Path()]):
    try:
        user = await user_service.delete_user_by_id(session=session,id=user_id)
        if user is not None:
            return {"deleted_id" : user}
        return "User not Exists"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )