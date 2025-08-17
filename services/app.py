from fastapi import FastAPI
from data_loader.data_loader import DataLoader
import os

app = FastAPI()

@app.get("/api/get_information/{table_name}")
async def get_information(table_name:str):
    """Fetch all records from the specified table."""
    data_loader = DataLoader()
    return data_loader.get_all(table_name)

def get_port():
    """Get the port number from environment variables."""
    app_port:str = os.getenv("APP_PORT") or ""
    if app_port.isdigit():
        return int(app_port)
    raise ValueError("Invalid port number")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=get_port())