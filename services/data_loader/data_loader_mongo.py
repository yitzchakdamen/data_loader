import os
import logging
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from bson import json_util
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class DataLoader:
    
    def __init__(self) -> None:
        """Initialize database connection parameters."""
        self.MONGO_HOST:str = os.getenv("MONGO_HOST") or ""
        self.MONGO_PORT:int = int(os.getenv("MONGO_PORT") or '0')
        self.MONGO_DATABASE:str = os.getenv("MONGO_DATABASE") or ""
        self.MONGO_INITDB_ROOT_USERNAME:str = os.getenv("MONGO_INITDB_ROOT_USERNAME") or ""
        self.MONGO_INITDB_ROOT_PASSWORD:str = os.getenv("MONGO_INITDB_ROOT_PASSWORD") or ""
        self.client_con = self.client()
        logger.debug(f"Database connection parameters set: DB_HOST:{self.MONGO_HOST}, MONGO_DATABASE:{self.MONGO_DATABASE}, MONGO_INITDB_ROOT_USERNAME:{self.MONGO_INITDB_ROOT_USERNAME}, MONGO_INITDB_ROOT_PASSWORD:{self.MONGO_INITDB_ROOT_PASSWORD}")

    def client(self) -> MongoClient:
        """
        Create a MongoDB client.
        """
        client_strung = f"mongodb://{self.MONGO_INITDB_ROOT_USERNAME}:{self.MONGO_INITDB_ROOT_PASSWORD}@{self.MONGO_HOST}:{ self.MONGO_PORT}"
        client:MongoClient = MongoClient(client_strung)
        return client
    
    def get_database(self) -> Database:
        """
        Create a database connection.
        """ 
        
        if self.MONGO_DATABASE not in self.client_con.list_database_names():
            raise ValueError(f"Database '{self.MONGO_DATABASE}' does not exist. Please check the configuration.")
            
        db: Database = self.client_con[self.MONGO_DATABASE]
        logger.debug("Database connection successful.")
        return db

    def get_all(self, collection: str) -> list:
        """
        Fetch all records from the specified table.
        """
        
        logger.debug(f"Fetching all records from collection: {collection}")

        db: Database = self.get_database()
        col: Collection = db[collection]

        docs = list(col.find({}))
        return json.loads(json_util.dumps(docs))
