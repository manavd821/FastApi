from fastapi import FastAPI
from ..utils import get_user_by_id

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/user/{id}")
async def read_item(id: int):
    user = await get_user_by_id(id)
    return user