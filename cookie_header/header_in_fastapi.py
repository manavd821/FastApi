from fastapi import FastAPI, Header 
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()

## Forbid extra cookie
class Product(BaseModel):
    model_config = {"extra": "forbid"} # imp for security purpose -  No extra info other than below given
    id : int
    name : str

# Validation is same as query para and path para
@app.get('/product')
async def get_product(user_agent : Annotated[str | None, Header()] = None):
    if user_agent:
        return {"user_agent": user_agent}
    return "No user agentfro