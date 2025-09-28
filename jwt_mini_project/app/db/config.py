from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection
from decouple import config
from fastapi import Depends
from typing import Annotated


DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_PORT = config("DB_PORT", cast = int)
DB_NAME = config("DB_NAME")
DB_HOST = config("DB_HOST")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(url=DB_URL, echo=True)

async def get_db_session():
    async with engine.connect() as session:
        yield session

DbSession = Annotated[AsyncConnection, Depends(get_db_session)]