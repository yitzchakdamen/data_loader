import os
import mysql.connector 

class DataLoader:
    
    def __init__(self) -> None:
        self.DB_HOST = os.getenv("DB_HOST")
        self.MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
        self.MYSQL_USER = os.getenv("MYSQL_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_PORT = 3306 # os.getenv("DB_PORT")
        

    def connector(self):
        return mysql.connector.connect(
            host=f"{self.DB_HOST}:{self.DB_PORT}",
            user=self.MYSQL_USER,
            password=self.DB_PASSWORD,
            database=self.MYSQL_DATABASE)

    def get_all(self, table:str) -> list:
        cursor = self.connector().cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result: list = cursor.fetchall()
        return result