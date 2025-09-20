from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Text
from app.db.base import Base

class User(Base):
    __tablename__ = 'user'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(Text, nullable=False)
    email : Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<User(id: {self.id}, name: {self.name}, email: {self.email})>" 