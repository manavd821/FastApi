from fastapi import FastAPI, Form
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
app = FastAPI()

# Form data - application/x-www-form-urlencoded

@app.post('/login')
async def login(username: Annotated[str, Form(min_length=3, max_length=20)],password: Annotated[str, Form(min_length=4, max_length=200)]):
    return {'username' : username,
            'pass_length' : len(password),
            'password' : password
            }
    
#With pydantic model
class FormData(BaseModel):
    username : str
    password : str 
    model_config= {'extra' : 'forbid'}
    
@app.post('/login2')
async def login2(data : Annotated[FormData, Form()]):
    return {'username' : data.username,
            'pass_length' : len(data.password),
            'password' : data.password,
            'data' : data
            }