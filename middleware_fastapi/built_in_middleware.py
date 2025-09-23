from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware

app = FastAPI()
# app.add_middleware(HTTPSRedirectMiddleware) # Redirect http request to https AND ws -> wss
app.add_middleware(TrustedHostMiddleware, allowed_hosts = ["localhost", "127.0.0.1"]) # only specified host will be allowed
# Response compress middlware is also available -> check it out

@app.get('/users')
async def home():
    print("I'm inside user endpoint")
    print("LALALALLALALALAL")
    return "Hare Krsna"