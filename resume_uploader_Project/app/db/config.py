from asyncio import futures
from ctypes import cast
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs,AsyncSession
from decouple import config
from fastapi import Depends
from typing import Annotated, AsyncGenerator



DB_USER=config("DB_USER")
DB_PASSWORD=config("DB_PASSWORD")
DB_HOST=config("DB_HOST")
DB_PORT=config("DB_PORT", cast=int)
DB_NAME=config("DB_NAME")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(DB_URL)

engine = create_async_engine(
    DB_URL, echo=True
)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, future=True)

class Base(DeclarativeBase, AsyncAttrs):
    pass

async def get_async_session() -> AsyncGenerator[async_sessionmaker, None]:
    async with async_session() as session:
        yield session

DbSession = Annotated[AsyncSession, Depends(get_async_session)]