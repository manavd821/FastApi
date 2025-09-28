from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.account.router import router as account_router
from app.account.tables import users as user_table, refresh_tokens as refresh_tokens_table


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:5500", "http://localhost:3000"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
    expose_headers = ["*"],
    max_age=86400
)

app.include_router(account_router)
