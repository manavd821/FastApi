from db import engine
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    phone: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"<User(id: {self.id}, name: {self.name}, email: {self.email})>"
    
