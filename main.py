```python
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Mount the static directory at the root with html=True
app.mount("/", StaticFiles(directory="static", html=True), name="static")

class FileUpload(BaseModel):
    name: str
    content: str
    description: Optional[str] = None

@app.post("/add-documentation")
async def upload_file(file_upload: FileUpload):
    try:
        with open(f"static/{file_upload.name}", "w") as f:
            f.write(file_upload.content)

        return JSONResponse(status_code=200, content={"message": "File has been uploaded successfully"})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```