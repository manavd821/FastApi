from db import create_tables
from models import User
from services import insert_user, get_all_user, get_user_by_id
create_tables()
# insert_user(name='Yug', email = "yug@email.com")
# result = get_all_user()
# print(result)
# print(type(result))

# result = get_user_by_id(id = 2)
# print(result)
# print(type(result))
