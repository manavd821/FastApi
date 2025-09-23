from fastapi import FastAPI

app = FastAPI()

# ASGI middleware are typically classes that take an ASGI app and configure parameters.
class CustomASGIMiddleware:
    def __init__(self, app, prefix = "LOG"):
        self.app = app
        self.prefix = prefix
    async def __call__(self, scope, receive, send):
        # scope: connection info (type, path, headers, etc.)
        # receive: async fn that gives incoming events (request body chunks, etc.)
        # send: async fn to send outgoing events (response headers, body, etc.)
        # print(f" scope : {scope}", end="\n\n\n\n\n")
        if scope["type"] == "http":  # only handle HTTP events
            print("Before processing request (ASGI middleware)")
        
        # call the next middleware or FastAPI app
        await self.app(scope, receive, send)
        
        if scope["type"] == "http":
            print(f"After processing request (ASGI middleware).")
            # print("\n\n\n\n scope = {scope}\n\n\n\n recieve: {receive}\n\n\n\n send: {send}")
            

# # Wrap FastAPI app inside your middleware
app.add_middleware(CustomASGIMiddleware, prefix = "My_LOG")

@app.get('/')
def home():
    print("I'm in my function. LALALLALA")
    return "Hare Krsna"