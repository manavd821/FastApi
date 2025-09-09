from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

db_url = 'sqlite:///./mydb.db'
engine = create_engine(url=db_url, echo=True)
metadata = MetaData()

# User table
users = Table(
    "users",
    metadata,
    Column("id",Integer, primary_key=True),
    Column("name",String(length=50), nullable=False),
    Column("email",String(length=50), nullable=False),
    # Column("phone",Integer, nullable=False, unique=True),
)
# posts table
# One to Many
posts = Table(
    "posts",
    metadata,
    Column("id",Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("title",String(length=50), nullable=False),
    Column("content",String(length=500), nullable=False)
)
# One to One
profile = Table(
    "profile",
    metadata,
    Column("id",Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True),
    Column("bio",String(length=50), nullable=False)
)
#Many to Many
# address = Table(
#     "address",
#     metadata,
#     Column("id",Integer, primary_key=True),
#     Column("street", Integer, ),
#     Column("country",String(length=50), nullable=False)
# )
# 

# create table in database
def create_table_bhai():
    metadata.create_all(engine)

# drop table
def drop_table_bhai():
    metadata.drop_all(engine)
    
if __name__ == "__main__":
    create_table_bhai()
    print("table created")