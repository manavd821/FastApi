from fastapi import FastAPI, Cookie
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()

## Forbid extra cookie
class Product(BaseModel):
    model_config = {"extra": "forbid"} # imp for security purpose -  No extra info other than below given
    id : int
    name : str

# Validation is same as query para and path para
@app.get('/products/recommandation')
async def  get_recommandations(session_id : Annotated[str | None, Cookie()] = None):
    if session_id:
        return {'session_id': session_id}
    return {'msg':'No session id provided'}
