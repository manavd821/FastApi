from db import engine, users, posts
from sqlalchemy import insert, update, delete, select, asc, desc, func

# insert
def create_user(name : str, email : str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email)
        conn.execute(stmt)
        conn.commit()
        
# create_user(name="Ramesh", email="ramesh@gmail.com")
# create_user(name="Yug", email="yug@gmail.com")

def create_posts(id : int,user_id : int, title : str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(id = id,user_id = user_id, title = title, content = content)
        conn.execute(stmt)
        conn.commit()

# create_posts(id=1, user_id=1, title="Devotee", content="Lallu che")
# create_posts(id=5, user_id=5, title="Gamer", content="Bholu che")
# create_posts(id=4, user_id=4, title="Ramesh che", content="Ramesh che bhai")

# get one user
def get_one_user(id : int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == id)
        result = conn.execute(stmt).first()
        return result

# result = get_one_user(3)
# print(type(result))
# print(result)

# get all user
def get_all_users():
    with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).fetchall()
        return result

# all_users = get_all_users()
# print(all_users)

# update 
def update_user_email(id : int, new_email : str):
    with engine.connect() as conn:
        stmt = update(users).where(users.c.id == id).values(email = new_email)
        conn.execute(stmt) 
        conn.commit()

# update_user_email(id=2, new_email='manav@gmail.com')

# delete 
def delete_user_by_id(id : int):
    with engine.connect() as conn:
        stmt = delete(users).where(users.c.id == id)
        conn.execute(stmt) 
        conn.commit()
        
# delete_user_by_id(id=2)

# Order by [A-Z, a-z]
def get_users_order_by_name():
    with engine.connect() as conn:
        stmt = select(users).order_by(desc(users.c.name))
        result = conn.execute(stmt).fetchall()
        return result
    
# result = get_users_order_by_name()
# print(type(result))
# print(result)

# group by
def get_user_group_by():
    with engine.connect() as conn:
        stmt = select(
                    users.c.name,
                    func.count(users.c.id).label("id_with_same_name")  
                    ).group_by(users.c.name)
        result = conn.execute(stmt).fetchall()
        return result
    
# result = get_user_group_by()
# # print(type(result))
# print(result)

# Join operations
def get_user_posts_join():
    with engine.connect() as conn:
        stmt = select(
                    posts.c.id,
                    users.c.name.label("author_name"),
                    posts.c.title
                    ).join(users, users.c.id == posts.c.id )
        result = conn.execute(stmt).fetchall()
        return result
    
result = get_user_posts_join()
# print(type(result))
print(result) 