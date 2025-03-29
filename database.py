import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.server_api import ServerApi

class Database:
    def __init__(self):
        try:
            self.client = MongoClient(os.environ["database-connection-string"], server_api=ServerApi('1'))
            self.database = self.client.get_database("HooHacks2025")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            self.client = None
            self.database = None

    def ping(self):
        if not self.client:
            return "Database connection not initialized."
        try:
            self.client.admin.command('ping')
            return "Database connection successful!"
        except ConnectionFailure as e:
            return f"Database connection failed: {e}"