from fastapi import FastAPI
from app.user import services as user_service
from pydantic import Field, BaseModel
app = FastAPI()

class UserCreate(BaseModel):
    name : str
    email : str
    
@app.post('/user')
def user_create(user : UserCreate):
    user_service.insert_user(name = user.name, email = user.email)
    return {"status" : "Success"}

@app.get('/users')
def get_all_users():
    users = user_service.get_all_user()
    return users


