from fastapi import FastAPI
from data_loader.data_loader import DataLoader

app = FastAPI()
data_loader = DataLoader()

@app.get("/api/get_information/{table_name}")
async def get_information(table_name:str):
    return data_loader.get_all(table_name)
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)