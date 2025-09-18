from db import User, Post, SessionLocal
from sqlalchemy import select, asc, desc
# Insert or create User
def insert_user(name : str, email : str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(instance=user)
        session.commit()
        session.refresh(user)
        return user
    
# result = insert_user(name="Yug", email="yug@email.com")
# print(result)

# Insert or create Posts
def insert_posts(user_id: int,title : str, content : str):
    with SessionLocal() as session:
        post = Post(user_id = user_id, title=title, content=content)
        session.add(instance=post)
        session.commit()
        session.refresh(post)
        return post
    
# result = insert_posts(user_id = 1, title='Manav title', content='Manav content')
# result = insert_posts(user_id = 2, title='Yug title', content='Yug content')
# print(result)

# select user
def get_user_by_id(user_id : int):
    with SessionLocal() as session:
        user = session.get_one(User, user_id)
        return user
    
# result = get_user_by_id(user_id=2)
# print(result)
# print(result.id)

def get_all_user():
    with SessionLocal() as session:
        user = session.query(User).all()
        return user
    
# result = get_all_user()
# print(result)
# print(type(result))

def get_user_by_id2(user_id : int):
    with SessionLocal() as session:
        user = session.query(User).filter_by(id=user_id).first()
        return user
    
# result = get_user_by_id2(user_id=2)
# print(result)
# print(type(result))

def get_post_by_id(id : int):
    with SessionLocal() as session:
        stmt = select(Post).where(Post.id == id)
        post = session.scalars(stmt).one_or_none()
        return post
    
# result = get_post_by_id(id=1)
# print(result)   

# get_all_users
def get_all_users():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users
    
# result = get_all_users()
# print(result)

# update
def update_user_email(user_id : int, new_email : str):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()
        return user
# print(update_user_email(1, 'manav2@gmail.com'))

# delete post
def delete_post(id : int):
    with SessionLocal() as session:
        post = session.get(Post,id )
        if post:
            session.delete(post)
            session.commit()

# delete_post(id=1)

# order by
def order_by_user():
    with SessionLocal() as session:
        stmt = select(User).order_by(desc(User.id))
        users = session.scalars(stmt).all()
        return users
    
# print(order_by_user())