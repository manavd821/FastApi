from fastapi import FastAPI
from router import router as user_router, router2 as product_router

app = FastAPI()
app.include_router(user_router, tags=["users"]) #Tag is for swagger UI
app.include_router(product_router, tags=["products"], prefix='/products') #Tag is for swagger UI

@app.get('/')
async def home():
    return "Hare Krsna"