from fastapi import FastAPI, BackgroundTasks
from typing import Annotated
import asyncio
app = FastAPI()

async def send_email(email : str, msg : str = ""):
    with open("log.txt", "w") as file:
        await asyncio.sleep(5)
        file.write(f"Email : {email}\n message : {msg}")

@app.get('/{email}')
async def home(email : str, background_task : BackgroundTasks):
    background_task.add_task(send_email, email = email, msg = "Hare Krsna Hare Krsna")
    return {
            "msg" :"Email sent"
        }