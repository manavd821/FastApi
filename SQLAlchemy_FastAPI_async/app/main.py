from fastapi import FastAPI
from app.user import services as user_services
from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    email : str
app = FastAPI()

@app.post('/user')
async def create_all_user(user : UserCreate):
    await user_services.insert_user(name = user.name, email=user.email)
    return {"status" : "Done Bhai"}

@app.get('/users')
async def get_users( ):
    users = await user_services.get_all_users()
    return users