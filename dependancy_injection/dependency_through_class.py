from fastapi import FastAPI, Depends
from typing import Annotated
app = FastAPI()

class My_Dependency:
    def __init__(self, id : int = 101, name : str = "Yug"):
        self.id = id
        self.name = name

@app.get('/')
async def home(user : Annotated[My_Dependency, Depends(My_Dependency)]):
    return {
            "Greet" :"Hare Krsna",
            "id" : user.id,
            "name" : user.name
        }