from fastapi import FastAPI, Depends
from typing import Annotated
app = FastAPI()

async def my_dependency(q : str, skip : str, limit : int):
    return {
        "q" : q,
        "skip" : skip,
        "limit" : limit
    }
    
My_Dep = Annotated[dict, Depends(my_dependency)]

@app.get('/')
async def home():
    return "Hare Krsna"

@app.get('/users')
async def get_users(abc : My_Dep):
    return abc