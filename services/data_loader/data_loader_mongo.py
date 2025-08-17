import os
import logging
import pymongo

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["database"]

logger.debug(db)
