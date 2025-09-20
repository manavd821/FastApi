from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Text
from app.db.base import Base

class User(Base):
    __tablename__ = 'product'
    produ_id : Mapped[int] = mapped_column(Integer, primary_key=True)
    produ_name : Mapped[str] = mapped_column(Text, nullable=False)
    price : Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User(produ_id: {self.produ_id}, produ_name: {self.produ_name}, price: {self.price})>" 