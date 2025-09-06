from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
app = FastAPI()


from fastapi.responses import HTMLResponse
# Serve a simple HTML page with file upload form
@app.get("/", response_class=HTMLResponse)
async def upload_form():
    return """
    <html>
        <head>
            <title>Upload File Practice</title>
        </head>
        <body>
            <h2>Upload a File</h2>
            <form action="/login4" enctype="multipart/form-data" method="post" multiple>
                <input type="file" name="files" multiple><br><br>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """


# Form data - multipart/formdata
@app.post('/login')
async def login(file: Annotated[bytes | None, File()] = None):
    if file:
        return {'file' : len(file)}
    return {'msg' : 'No file uploaded'}

# to store file
import os, uuid
@app.post('/login2')
async def login2(file: Annotated[bytes | None, File()] = None):
    if file:
        filename = f"{uuid.uuid4()}.bin"
        save_path = f"uploads/{filename}"
        os.makedirs('uploads', exist_ok = True)
        
        with open(save_path, "wb") as f:
            f.write(file)
        return file
    return {'msg' : 'No file uploaded'}


# Use of UploadFile - You can save img as well
import shutil
@app.post('/login3')
async def login3(file : Annotated[UploadFile | None, File()] = None):
    if file:
        save_path = f'uploads/{file.filename}'
        os.makedirs('uploads', exist_ok=True)
        
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(fsrc=file.file, fdst=f)
        return file
    return {'msg' : 'No file uploaded'}

# Upload multiple file
@app.post('/login4')
async def login4(files : Annotated[List[UploadFile] | None, File()] = None):
    if files:
        os.makedirs('uploads', exist_ok=True)
        save_file = []
        for file in files:
            save_path = f'uploads/{file.filename}'
            with open(save_path, 'wb') as f:
                shutil.copyfileobj(fsrc=file.file, fdst=f)
            save_file.append({'filename': file.filename})
        return save_file
    return {'msg' : 'No file uploaded'}