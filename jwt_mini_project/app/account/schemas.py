from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name : str
    password : str = Field(min_length=5)  # matches bcrypt hash length
    is_admin: bool = False
    is_active: bool = True
    is_verified: bool = False
    
class User(UserCreate):
    user_id : int
    
    
    
    