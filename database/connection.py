from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from database.config import MONGO_URI, DATABASE_NAME

try:
    client = MongoClient(MONGO_URI)

    # Verify connection
    client.admin.command("ping")

    db = client[DATABASE_NAME]

    print("✅ Connected to MongoDB")

except ConnectionFailure:
    print("❌ Could not connect to MongoDB")