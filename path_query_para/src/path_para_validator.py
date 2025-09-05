from fastapi import FastAPI, Query
from typing import Annotated
app = FastAPI()
products = [
    {
        "id": 1,
        "name": "Laptop",
        "brand": "Dell",
        "price": 65000,
        "in_stock": True,
        "tags": ["electronics", "computer", "work"]
    },
    {
        "id": 2,
        "name": "Smartphone",
        "brand": "Samsung",
        "price": 25000,
        "in_stock": False,
        "tags": ["electronics", "mobile", "android"]
    },
    {
        "id": 3,
        "name": "Headphones",
        "brand": "Sony",
        "price": 4000,
        "in_stock": True,
        "tags": ["electronics", "audio", "music"]
    },
    {
        "id": 4,
        "name": "Backpack",
        "brand": "Wildcraft",
        "price": 1800,
        "in_stock": True,
        "tags": ["accessories", "travel", "bag"]
    }
]

from fastapi import Path

@app.get('/products/{product_id}')
async def update_product(product_id : Annotated[int, Path(ge=1, description='Integer value', title='id che bhai')]):
    return {"msg": "Msg",
            "product_id": product_id,
            "new_product": 'new_product'}
    