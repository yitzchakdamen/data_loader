from pydantic import BaseModel

class MysqlRow(BaseModel):
    """Represents a row of data the relevant columns"""
    ID: int
    first_name: str
    last_name: str

    