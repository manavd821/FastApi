import asyncio
import itertools
import time
from fastapi import FastAPI, Request, Response
import json
from fastapi.responses import StreamingResponse, PlainTextResponse
from datetime import datetime
import aiofiles

app = FastAPI()
@app.get('/', response_class=PlainTextResponse)
async def main():
    response = PlainTextResponse(
        content="Hare Krsna",
        media_type='text/plain',
        headers = {
        'Content-Type' : 'text/plain',
        },
    )
    
    return response

headers = {
    'Content-Type' : 'text/event-stream',
    'Connection' : 'keep-alive',
    'Cache-Control' : 'no-cache',
}
async def event_stream(request: Request):
    conter = 1
    last_event = time.perf_counter()
    while True:
        # handling disconnection
        if await request.is_disconnected():
            print("Client disconnected ❌")
            break
        # timeout handling
        if time.perf_counter() - last_event > 25:
            print("Connection timed out ⚠️")
            break
        if conter == 5:
            yield "event: end\ndata: Stream completed\n\n"
            break
        
        await asyncio.sleep(1.5)
        conter += 1
        data = {"msg": "hello", "count": conter}
        json_data = json.dumps(data)
        yield f"data: {json_data}\n\n"
        last_event = time.perf_counter()
        
@app.get('/api/events')
async def main(response : Response, request : Request):
    # response.headers.update(headers)
    return StreamingResponse(event_stream(request), headers=headers, media_type='text/event-stream')

@app.get('/photo')
async def photo_mangta():
    async def file_iterator():
        start = time.perf_counter()
        counter = itertools.count()
        async with aiofiles.open("book.pdf", "rb") as f:
            while True:
                chunk = await f.read(1024)
                if not chunk:
                    print("finished in ", time.perf_counter() - start)
                    break
                yield chunk
                print("sending chunk...", next(counter))
    return StreamingResponse(file_iterator(), headers=headers ,media_type='application/pdf')