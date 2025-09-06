from fastapi import FastAPI, Response
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
app = FastAPI()

class Product(BaseModel):
    id: int = Field(..., description="Unique product ID", gt=0)
    name: str = Field(..., min_length=3, max_length=50, description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    in_stock: bool = Field(default=True, description="Availability status")
    description: Optional[str] = Field(None, max_length=200, description="Short description of the product")

# validate return type
@app.get('/product')
async def get_products() -> List[Product]:
    return [
                {
                    "id" : 1,
                    'name' : 'Manav',
                    'price' : 150,
                    'in_stock' : True,
                    'description' : 'Hare Krsna',
                    "status" : "ok" # It is not mentioned in Product -> It will not be returned in response body
                }
            ]
    
# Best Practice :-
# with re_model para -> Decorator no parameter
@app.get('/product/res', response_model=Product)
async def get_products_res() :
    return   {
                    "id" : 1,
                    'name' : 'Manav',
                    'price' : 150,
                    # 'in_stock' : True,
                    'description' : 'Hare Krsna',
                    "status" : "ok" # It is not mentioned in Product -> It will not be returned in response body
                }
            
# To remove default values in response
# some field are not in response and has default value in pydantic model, if we want to remove that field
# By using 'response_model_exclude_unset', 'in_stock' field has defalut value true but if we don't pass it in return dict, it will not go
@app.get('/product/res2', response_model=Product, response_model_exclude_unset=True)
async def get_products_res2() :
    return   {
                    "id" : 1,
                    'name' : 'Manav',
                    'price' : 150,
                    # 'in_stock' : True,
                    'description' : 'Hare Krsna',
                    "status" : "ok" # It is not mentioned in Product -> It will not be returned in response body
                }
            
# It will return only name and price
@app.get('/product/res3', response_model=Product, response_model_include={"name","price"})
async def get_products_res3() :
    return   {
                    "id" : 1,
                    'name' : 'Manav',
                    'price' : 150,
                    # 'in_stock' : True,
                    'description' : 'Hare Krsna',
                    "status" : "ok" # It is not mentioned in Product -> It will not be returned in response body
                }

# It will remove name and price from response body
@app.get('/product/res4', response_model=Product, response_model_exclude={"name","price"})
async def get_products_res4() :
    return   {
                    "id" : 1,
                    'name' : 'Manav',
                    'price' : 150,
                    # 'in_stock' : True,
                    'description' : 'Hare Krsna',
                    "status" : "ok" # It is not mentioned in Product -> It will not be returned in response body
                }
    