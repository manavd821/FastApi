from fastapi import FastAPI
from app.log_config import logger
app = FastAPI()

@app.get('/')
def root():
    logger.info("Root endpoint access")
    logger.warning("Root endpoint access warning")
    return {'msg' : 'hare Krsna'}

@app.get('/get')
def get_data():
    return {'get' : 'Data'}