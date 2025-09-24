from fastapi import FastAPI, Depends, Header, HTTPException, status
from typing import Annotated

async def my_dependency(q : str, skip : str, limit : int):
    return {
        "q" : q,
        "skip" : skip,
        "limit" : limit
    }
# app = FastAPI(dependencies=[my_dependency]) # for global dependeny
app = FastAPI()

async def verify_token(x_token : Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "X-toke Header Invalid"
            )

@app.get('/', dependencies=[Depends(verify_token)])
async def home():
    return {
            "Greet" :"Hare Krsna"
        }