from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db_path = os.path.join(file_path, "mydb.db")

URL = f"sqlite+aiosqlite:///{db_path}"
engine = create_async_engine(URL, echo = True)
sessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)