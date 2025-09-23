from fastapi import FastAPI, middleware, Request

app = FastAPI()
#Key points :
# - middleware executes from bottom to top


# First middleware
# @app.middleware("http")
# async def my_first_middleware(request : Request, call_next):
#     print("Middleware 1st: Before Proccesing the request")
    
#     response = await call_next(request)
#     print(f"Bhai response: {response}")
    
#     print('Middlaware 1st. After procceding the request, before returning the response')
    
#     return response

# # Second middleware
# @app.middleware("http")
# async def my_second_middleware(request : Request, call_next):
#     print("Middleware 2nd: Before Proccesing the request")
    
#     response = await call_next(request)
#     print(f"Bhai response: {response}")
    
#     print('Middlaware 2nd. After procceding the request, before returning the response')
    
#     return response


async def only_for_user_middleware(request: Request, call_next):
    if request.url.path.startswith('/users'):
        print("User Middleware 2nd: Before Processing the request")

    response = await call_next(request)

    if request.url.path.startswith('/users'):
        print(f"Bhai response: {response}")
        print("User Middleware 2nd: After Processing, before returning response")

    return response

# middleware only for users
app.middleware('http')(only_for_user_middleware)


@app.get('/users')
async def home():
    print("I'm inside user endpoint")
    print("LALALALLALALALAL")
    return "Hare Krsna"

@app.get('/products')
async def home():
    print("I'm inside product endpoint")
    print("LALALALLALALALAL")
    return "Hare Krsna"