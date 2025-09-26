from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

template = Jinja2Templates(directory= TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
async def home_page(request : Request):
    return template.TemplateResponse(
        request=request,
        name = "home_page.html",
        context= {
            "name" : "Manav",
            "greet" : "Hare Ram"
        }
    )