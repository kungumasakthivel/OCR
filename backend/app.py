from fastapi import FastAPI, UploadFile, File
import uvicorn
import shutil
from pathlib import Path
from ipynb.fs.full.function_text import text_extract

app = FastAPI()

@app.get('/')
def home():
    return {
        "message": "api is working"
    }


@app.post('/file/upload')
def upload_file(file: UploadFile):
    upload_folder = Path("uploads")
    upload_folder.mkdir(exist_ok=True)
    file_path = upload_folder / file.filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    words = text_extract(file_path)
    
    return {
        "filename": file_path, 
        "words": words
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
