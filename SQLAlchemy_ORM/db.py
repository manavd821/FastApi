from sqlalchemy import create_engine, Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship

database_url = "sqlite:///sqlite.db"
engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Base class
class Base(DeclarativeBase):
    pass


# Association table for many-to-many
user_address_association = Table(
    "user_address_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"), primary_key=True),
)


# User model
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # One to many: User -> Post
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete")

    # One to one: User -> Profile
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete")

    # Many to many: User <-> Address
    addresses: Mapped[list["Address"]] = relationship(
        "Address",
        secondary=user_address_association,
        back_populates="users",
        cascade="all, delete"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# Post model (One-to-Many)
class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    
    user: Mapped["User"] = relationship("User", back_populates="posts")
    
    def __repr__(self) -> str:
        return f"<Post(id={self.id!r}, title={self.title!r})>"


# Profile model (One-to-One)
class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    
    user: Mapped["User"] = relationship("User", back_populates="profile")
    
    def __repr__(self) -> str:
        return f"<Profile(id={self.id!r}, title={self.title!r})>"


# Address model (Many-to-Many)
class Address(Base):
    __tablename__ = "address"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[list["User"]] = relationship(
        "User",
        secondary=user_address_association,
        back_populates="addresses"
    )
    
    def __repr__(self) -> str:
        return f"<Address(id={self.id!r}, street={self.street!r})>"

# Create table
def create_tables():
    Base.metadata.create_all(engine)
# Drop tables
def drop_tables():
    Base.metadata.drop_all(engine)
    
if __name__ == '__main__':
    create_tables()
    # drop_tables()