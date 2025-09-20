from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, Integer, Float

class Product(Base):
    __tablename__ = 'product'
    prod_id : Mapped[int] = mapped_column(Integer, primary_key=True)
    prod_name : Mapped[str] = mapped_column(Text, nullable=False)
    price : Mapped[float] = mapped_column(Float, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User(prod_id: {self.prod_id}, prod_name: {self.prod_name}, price: {self.price})>" 