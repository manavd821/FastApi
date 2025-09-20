from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
URL = "sqlite+aiosqlite:///mydb.db"
engine = create_async_engine(url=URL, echo = True)

asych_session = async_sessionmaker(bind=engine,expire_on_commit=False)
