from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from decouple import config
from sqlalchemy.orm import DeclarativeBase
# from alembic import context

DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT", cast = int)
DB_NAME = config("DB_NAME")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DB_URL, echo = True, future = True)
SessionLocal = async_sessionmaker(bind = engine, expire_on_commit=False)

# alembic_config = context.config
# alembic_config.set_main_option("sqlalchemy.url", DB_URL)

class Base(DeclarativeBase, AsyncAttrs):
    pass


from app.user import models as user_models

