from sqlalchemy.ext.asyncio import create_async_engine

URL = "sqlite+aiosqlite:///mydb.db"
engine = create_async_engine(url=URL, echo = True)

