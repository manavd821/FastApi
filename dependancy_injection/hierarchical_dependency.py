from fastapi import FastAPI, Depends
from typing import Annotated
app = FastAPI()

async def user_auth():
    return {"name" : "Manav"}

async def user_role(user : Annotated[dict, Depends(user_auth)]):
    return{
        "id" : 123,
        "name" : user["name"]
    }

@app.get('/')
async def home(user : Annotated[dict, Depends(user_role)]):
    return {
            "Greet" :"Hare Krsna",
            "id" : user["id"],
            "name" : user["name"]
        }