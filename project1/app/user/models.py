from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, String, ForeignKey
from app.db.config import Base

class User(Base):
    __tablename__ = 'user'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(Text, nullable=False)
    email : Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="user")

    
    def __repr__(self):
        return f"<User(id: {self.id}, name: {self.name}, email: {self.email})>" 
    
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    street: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    state: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    
    user: Mapped["User"] = relationship("User", back_populates="addresses")
