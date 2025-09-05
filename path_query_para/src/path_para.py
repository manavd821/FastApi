from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return {"msg" : "Hare Krnsa"}

@app.get('/products')
async def all_product():
    return {'pr':"bhao"}

@app.post('/products')
async def create_product(new_product : dict):
    return {"msg": "Hare Krsna",
            "new_product": new_product}

# complete data update
@app.put('/products/{product_id}')
async def update_product(new_product : dict, product_id : int):
    return {"msg": "Compelete data update",
            "product_id": product_id,
            "new_product": new_product}
    
# partial data update
@app.patch('/products/{product_id}')
async def partial_update_product(new_product : dict, product_id : int):
    return {"msg": "partial data update",
            "product_id": product_id,
            "new_product": new_product}
    
    
# Restrict to certain set of predifined values 
# parameters are case-sensetive, take care of it
from enum import Enum
class Product(str, Enum):
    books = "books",
    cloth = "cloth",
    branch = "branch"
    
# example 1 
@app.get('/products/{new_product}')
async def Restrict_to_certain(new_product : Product):
    return {"msg": "partial data update",
            "new_product": new_product}
# example 2
@app.get('/category/{category}')
async def get_product(category : Product):
    if category == Product.books :
        return {"category": category,
                "msg": "Books are awesome"}
    elif category.value == "cloth" :
        return {"category": category,
                "msg": "clothes are awesome"}
    elif category == Product.branch.value:
        return {"category": category,
                "msg": "branch are awesome"}    
    else: 
        return {"category": category,
                "msg": "unknown category"} 