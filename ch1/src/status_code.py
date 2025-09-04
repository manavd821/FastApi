from fastapi import FastAPI, status
app = FastAPI()

@app.get('/', status_code=200)
async def all():
    return {'name':'Manav'}


@app.get('/home', status_code=status.HTTP_200_OK)
async def home_page():
    return {'name':'Manav', 'status' : 'Done'}
