from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Path
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
class ConnectionManager:
    def __init__(self):
        self.active_connection : list[WebSocket] = []
    # connect
    async def connect(self, websocket : WebSocket):
        await websocket.accept()
        self.active_connection.append(websocket)
    # dissconnect
    def disconnect(self, websocket : WebSocket):
        self.active_connection.remove(websocket)
    # get msg from client
    async def recieve_msg(self, websocket : WebSocket):
        return await websocket.receive_text()
    # send msg to client
    async def send_personal_msg(self, websocket : WebSocket, msg : str = ""):
        await websocket.send_text(msg)
    # broadcast to all client
    async def broadcast_msg(self, msg : str = ""):
        for connection in self.active_connection:
            await connection.send_text(msg)

@app.get('/')
async def home():
    return HTMLResponse(html)

manager = ConnectionManager()

@app.websocket('/ws/{client_id}')
async def websocket_endpoint(websocket : WebSocket, client_id : Annotated[int, Path()]):
    await manager.connect(websocket=websocket)
    try:
        while True:
            data = await manager.recieve_msg(websocket)
            await manager.send_personal_msg(websocket, msg = f"You wrote bhai: {data}")
            await manager.broadcast_msg(msg = f"Message from {client_id} : {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast_msg(f"client with id {client_id} left the chat")
        