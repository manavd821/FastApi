from fastapi import FastAPI
from app.account.router import router as account_router
from app.account.tables import users as user_table, refresh_tokens as refresh_tokens_table


app = FastAPI()
app.include_router(account_router)
