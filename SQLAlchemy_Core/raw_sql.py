from db import engine, users, posts
from sqlalchemy import text

# insert
def insert_user(name : str, email : str):
    with engine.connect() as conn:
        stmt = text("""
                    insert into users (name, email)
                    values (:name, :email)
                """)
        conn.execute(stmt,{"name" : name, "email":email})
        conn.commit()

# insert_user(name="sonam", email="sonam@email.com")

# select
def get_single_users(id : int):
    with engine.connect() as conn:
        stmt = text("""
                    select * from users
                    where id = :id
                """)
        result =conn.execute(stmt, {"id" : id}).fetchall()
        return result
        
        
result = get_single_users(id=4)
print(result)