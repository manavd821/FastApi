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


@app.get('/')
async def home():
    return {"msg" : "Hare Krnsa"}

# without Annotated (old version)
@app.get('/products/old')
async def show_product(search : str | None = Query(default=None, max_length=5)):
    if search:
        lower_search = search.lower()
        filtered_product = []
        for product in products:
            if lower_search in product['name'].lower():
                filtered_product.append(product)
        return filtered_product
    return {"msg" : "Hare Krnsa"}

# with Annotated
@app.get('/products/new')
async def show_product_2(search : Annotated[str | None , Query(max_length=5)] = None):
    if search:
        lower_search = search.lower()
        filtered_product = []
        for product in products:
            if lower_search in product['name'].lower():
                filtered_product.append(product)
        return filtered_product
    return {"msg" : "Hare Krnsa"}

# add regular expression
@app.get('/products/reg')
async def show_product_3(search : Annotated[str | None , Query(max_length=5, pattern="^[a-z]+$")] = None):
    if search:
        lower_search = search.lower()
        filtered_product = []
        for product in products:
            if lower_search in product['name'].lower():
                filtered_product.append(product)
        return filtered_product
    return {"msg" : "Hare Krnsa"}

# # Multiple search term(List)
@app.get('/products/get')
async def get_products(search : Annotated[list[str] | None , Query(max_length=5,
                                                                   alias='q',
                                                                   description='search by product name',
                                                                   title='Search product',
                                                                   deprecated=True)] = None):
    if search:
        filtered_product = []
        for product in products:
            for s in search:
                if s.lower() in product['name'].lower():
                    filtered_product.append(product)
        return filtered_product
    return products

# Custom validation
from pydantic import AfterValidator
def check_id(id: str):
    if not id.startswith("prod-"):
        raise ValueError("Id must start with 'prod-'")
    return id

@app.get('/product/check')
async def product_get(id : Annotated[str | None, AfterValidator(check_id)] = None):
    if id:
        return {'id' : id, 'msg': 'valid id'}
    return {'msg': 'Not a valid id'}
    