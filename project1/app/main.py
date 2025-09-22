from app.user import services as user_service
import asyncio
async def main():
    # await user_service.insert_user(name="heet", email="heet@email.com")
    await user_service.insert_address(street="B-5", city="Surat", state="Guj", user_id=1)
    print("Done Bhai")
    # user_address = await user_service.get_all_user()
    

    
asyncio.run(main())