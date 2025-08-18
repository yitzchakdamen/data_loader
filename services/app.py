from fastapi import FastAPI
from data_loader.data_loader_mysql import DataLoader as MysqlDataLoader
from data_loader.data_loader_mongo import DataLoader as MongoDataLoader
from model.data_row import MysqlRow
import os
import logging

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.get("/api/get_information/mysql/{table_name}", response_model=list[MysqlRow])
async def get_information_mysql(table_name:str):
    """Fetch all records from the specified table."""
    
    logger.debug(f"Fetching all records from MySQL table: {table_name}")
    data_loader = MysqlDataLoader()
    return data_loader.get_all(table_name)

@app.get("/api/get_information/mongo/{collection}")
async def get_information_mongo(collection:str):
    """Fetch all records from the specified table."""
    
    logger.debug(f"Fetching all records from MongoDB collection: {collection}")
    data_loader = MongoDataLoader()
    return data_loader.get_all(collection)

def get_port():
    """Get the port number from environment variables."""
    app_port:str = os.getenv("APP_PORT") or ""
    if app_port.isdigit():
        return int(app_port)
    raise ValueError("Invalid port number")

if __name__ == "__main__":
    loader = MongoDataLoader()
    loader.init_data(
        collection="users",
        initial_data=[{"username": "admin", "password": "1234"},{"username": "user", "password": "abcd", "email": "user@example.com"}]
    )
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=get_port())  
    
