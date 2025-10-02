from fastapi import FastAPI
from decouple import config

app = FastAPI()

DB_USER = config("DB_USER")

@app.get('/')
async def home():
    return f"Hare Krsna Hare Ram Ram Ram Hare Hare Krsna Krsna Ram {DB_USER}"
@app.get('/product')
async def product_page():
    return "Product page Hare Krsna"