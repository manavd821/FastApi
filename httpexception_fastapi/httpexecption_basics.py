from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
app = FastAPI()

item = {
    'apple' : 'Costly',
    'banana' : 'cheap'
}
@app.get('/{item_id}')
async def get_item(item_id : Annotated[str | None, Path()]):
    if item_id not in item:
        raise HTTPException(status_code=404, detail='Item not found',headers={'x-error-type' : 'itemNotFound'})
    return item[item_id]

# Custom Exception
class ItemException(Exception):
    def __init__(self, item_name : str):
        self.item_name = item_name

@app.exception_handler(ItemException)
async def handle_item_exception(req : Request, exe : ItemException):
    return JSONResponse(
        status_code=418,
        content={'msg' : f'{exe.item_name} not found'},
    )

@app.get('/item/{item_id}')
async def get_item2(item_id : Annotated[str | None, Path()]):
    if item_id not in item:
        raise ItemException(item_name=item_id)
    return item[item_id]    

# from fastapi.exceptions import RequestValidationError