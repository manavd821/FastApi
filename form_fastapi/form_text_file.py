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
        <h2>Upload Files with Login</h2>
        <form action="/login" enctype="multipart/form-data" method="post">
            <label>Username:</label><br>
            <input type="text" name="username" required><br><br>

            <label>Password:</label><br>
            <input type="password" name="password" required><br><br>

            <label>Select files:</label><br>
            <input type="file" name="files" multiple><br><br>

            <input type="submit" value="Upload">
        </form>
    </body>
</html>
    """
import shutil
@app.post('/login')
async def login_form(
    username : Annotated[str | None, Form()] = None,
    password : Annotated[str | None, Form()] = None,
    files : Annotated[List[UploadFile] | UploadFile |None , File()] = None
):
    # for files
    if files:
        save_file = []
        for file in files:
            save_path = 'uploads/{file.filename}'
            with open(save_path, 'wb') as f:
                shutil.copyfileobj(file.file, f)
            save_file.append({'filename':{file.filename}})
    
    return {'username' : username,
            'password' : password,
            'save_file': save_file}
