from sqlalchemy import MetaData, String, Integer, Table, Column
from db import engine

metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id",Integer, primary_key=True),
    Column("name",String(length=50), nullable=False),
    Column("email",String(length=50), nullable=False)
)
