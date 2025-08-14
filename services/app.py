from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

@app.get("/api/get_information")
async def get_information():
    return "hii"

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.1.0.0", port=8888)