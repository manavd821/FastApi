from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

class Product(BaseModel):
    id : int = Field(default=1, ge=3, le=10, title='ID', description='Write product id')
    name : str = Field(default='Manav', min_length=3, max_length=10)
    price : float

# Either use example in Field() Or Use below 
    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "id" : "1",
                    "name" : "Laptop",
                    "price" : "150"
                }
            ]
        }
    }

class Seller(BaseModel):
    name : str = Field(examples=['Krsna'])
    userName : str  = 'Manav'
    product : Product | None = Field(default=None)

# validated body
@app.post('/product')
async def validated_body(new_product : Product):
    print(new_product.id)
    print(new_product.name)
    print(new_product.price)
    return new_product

# edited validated body
@app.post('/product/new')
async def edited_validated_body(new_product : Product):
    product_dict = new_product.model_dump() # converts pydantic model into python dict
    price_with_text = new_product.price + (new_product.price * 0.18)
    product_dict.update({'price_with_text': price_with_text})
    return product_dict

# multiple body para
@app.post('/product/new2')
async def multiple_body_para(new_product : Product, seller : Seller):
    return {'new_product' : new_product,
            'seller' : seller}
    
# make body optional
@app.post('/product/new3')
async def make_body_optional(new_product : Product, seller : Seller | None = None):
    return {'new_product' : new_product,
            'seller' : seller}
    
# Singular value in body
@app.post('/product/new4')
async def Singular_value_in_body(new_product : Product,
                            seller : Seller,
                            secret_key : Annotated[str, Body()]):
    return {'new_product' : new_product,
            'seller' : seller,
            'secret_key': secret_key}
    
# Embed a Single body para
@app.post('/product/new5')
async def Embed_Body_para(new_product : Annotated[Product, Body(embed='product')]):
    return new_product
