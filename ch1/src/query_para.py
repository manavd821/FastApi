from fastapi import FastAPI
app = FastAPI()

@app.get('/products')
async def pr(sort : int = 2, boolian : bool = False, name : str | None = None):
    if not name:
        return {'sort' : sort, 'boolian' : boolian} # sort and boolian are query parameter if they are not in path parameter
    else:
        return {'sort' : sort, 'boolian' : boolian, 'name' : name} # sort and boolian are query parameter if they are not in path parameter
        
