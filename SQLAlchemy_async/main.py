from tables import create_table, drop_table
from queries import *
import asyncio

async def main():
    # await create_table()
    # await create_user(name='zeel', email='zeel@gmail.com')
    print(await get_user_by_id(id=3))
    await update_user_email(id=3, new_email='mnc@email.com')
    print(await get_user_by_id(id=3))

asyncio.run(main())