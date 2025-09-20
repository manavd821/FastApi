from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, Integer, Text
from sqlalchemy.ext.asyncio import AsyncAttrs
from db import engine

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(Text, nullable=False)
    email : Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User(id: {self.id}, name: {self.name}, email: {self.email})>" 
    
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
