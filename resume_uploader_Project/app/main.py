from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.resume.routers import router
from pathlib import Path
app = FastAPI()
app.include_router(router)


BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = BASE_DIR / "uploads"
app.mount('/uploads', StaticFiles(directory=UPLOAD_DIR))

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def home():
    return "Hare Krsna Hare Ram Hare Krsna"