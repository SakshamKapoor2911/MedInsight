import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.server_api import ServerApi

class Database:
    def __init__(self):
        try:
            self.client = MongoClient(os.environ["database-connection-string"], server_api=ServerApi('1'))
            self.database = self.client.get_database("main")
        except Exception as e:
            print(f"---ERROR--- Failed to connect to MongoDB: {e}")
            self.client = None
            self.database = None

    def ping(self):
        if not self.client:
            return "Database connection not initialized."
        try:
            self.client.admin.command('ping')
            return "Database connection successful!"
        except ConnectionFailure as e:
            return f"---ERROR--- Database connection failed: {e}"

    def get_doctors(self, latitude, longitude, specialty=None):
        parameters = {
            "latitude": { "$lt": latitude + 0.1, "$gt": latitude - 0.1 },
            "longitude": { "$lt": longitude + 0.1, "$gt": longitude - 0.1 },
        }

        if latitude is None or longitude is None:
            return "Request must contain latitude and longitude", 400

        query = self.database.database.doctors.find(
            parameters,
            {"_id": 0}
        )

        doctors = []
        for doctor in query:
            doctor["distance"] = ((doctor["latitude"] - latitude) ** 2 + (doctor["longitude"] - longitude) ** 2) ** 0.5
            doctors.append(doctor)
        doctors.sort(key=lambda x: x["distance"])

        if specialty:
            regex_conditions = [{"specialty": {"$regex": word, "$options": "i"}} for word in specialty.split()]
            parameters["$or"] = regex_conditions

        query = self.database.doctors.find(
            parameters,
            {"_id": 0}
        )

        doctors = []
        for doctor in query:
            doctor["distance"] = ((doctor["latitude"] - latitude) ** 2 + (doctor["longitude"] - longitude) ** 2) ** 0.5
            doctors.append(doctor)
        doctors.sort(key=lambda x: x["distance"])

        return doctors

    def get_health_centers(self, latitude, longitude):
        parameters = {
            "latitude": { "$lt": latitude + 0.1, "$gt": latitude - 0.1 },
            "longitude": { "$lt": longitude + 0.1, "$gt": longitude - 0.1 },
        }

        query = self.database.health_centers.find(
            parameters,
            {"_id": 0}
        )

        health_centers = []
        for health_center in query:
            health_center["distance"] = ((health_center["latitude"] - latitude) ** 2 + (health_center["longitude"] - longitude) ** 2) ** 0.5
            health_centers.append(health_center)
        health_centers.sort(key=lambda x: x["distance"])

        return health_centers