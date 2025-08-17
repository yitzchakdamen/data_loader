import os
import logging
import pymysql

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class DataLoader:
    
    def __init__(self) -> None:
        """Initialize database connection parameters."""
        self.DB_HOST:str = os.getenv("DB_HOST") or ""
        self.MYSQL_DATABASE:str = os.getenv("MYSQL_DATABASE") or ""
        self.MYSQL_USER:str = os.getenv("MYSQL_USER") or ""
        self.DB_PASSWORD:str = os.getenv("MYSQL_PASSWORD") or ""
        
        logger.debug(f"Database connection parameters set: DB_HOST:{self.DB_HOST}, MYSQL_DATABASE:{self.MYSQL_DATABASE}, MYSQL_USER:{self.MYSQL_USER}, MYSQL_PASSWORD:{self.DB_PASSWORD}")

    def connector(self):
        """Create a database connection.""" 
        connect = pymysql.connect(
            host=self.DB_HOST,
            user=self.MYSQL_USER,
            password=self.DB_PASSWORD,
            database=self.MYSQL_DATABASE,
            cursorclass=pymysql.cursors.DictCursor)
        
        if not connect:
            raise ConnectionError("Could not connect to the database.")
        
        logger.debug("Database connection successful.")
        return connect

    def get_all(self, table: str) -> tuple:
        """Fetch all records from the specified table."""
        logger.debug(f"Fetching all records from table: {table}")
        
        with self.connector() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table}")
                result:tuple = cursor.fetchall()
        return result 
