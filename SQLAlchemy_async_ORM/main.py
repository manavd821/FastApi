from model import create_table, drop_table
from db import asych_session
import asyncio
from quries import *

async def main():
    # await create_table()
    await insert_user(name = 'yug', email = 'yug@email.com')
asyncio.run(main())