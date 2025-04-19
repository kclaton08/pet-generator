import os
import sys
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from models.animal_record import AnimalRecord

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DatabaseGateway:
    def __init__(self, client: MongoClient) -> None:
        self.client = client
        self.db = client.PetGeneratorCluster
        self.collection = self.db.Animals

    def insert_data(self, data: AnimalRecord) -> None:
        try:
            self.collection.insert_one(data)
            logger.info("Data inserted successfully.")
        except Exception as e:
            logger.error("Error inserting data: %s", e)

    def find_data(self, query: dict, limit: int) -> list:
        try:
            return list(self.collection.find(query, limit=int(limit)))
        except Exception as e:
            logger.error("Error finding data: %s", e)
            return []

try:
    mongo = MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING"), serverSelectionTimeoutMS=5000)
    db = DatabaseGateway(mongo)
    logger.info("MongoDB connection successful: %s", mongo.server_info())
except ConnectionFailure as error:
  logger.error("MongoDB connection error: %s", error)
  sys.exit(1)









