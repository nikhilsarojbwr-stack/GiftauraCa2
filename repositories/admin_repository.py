# repositories/admin_repository.py

from database.connection import db


class AdminRepository:
    """
    Repository responsible for all MongoDB operations
    related to admin accounts.
    """

    def __init__(self):
        self.collection = db["admins"]

    # ============================================================
    # Find admin by username
    # ============================================================

    def find_by_username(self, username: str):
        return self.collection.find_one({
            "username": username
        })

    # ============================================================
    # Find admin by email
    # ============================================================

    def find_by_email(self, email: str):
        return self.collection.find_one({
            "email": email
        })

    # ============================================================
    # Find admin by username OR email
    # ============================================================

    def find_by_username_or_email(self, login: str):
        return self.collection.find_one({
            "$or": [
                {"username": login},
                {"email": login}
            ]
        })

    # ============================================================
    # Find admin by MongoDB ID
    # ============================================================

    def find_by_id(self, admin_id):
        from bson import ObjectId

        try:
            return self.collection.find_one({
                "_id": ObjectId(admin_id)
            })
        except Exception:
            return None

    # ============================================================
    # Create admin
    # ============================================================

    def create_admin(self, admin_data: dict):
        result = self.collection.insert_one(admin_data)

        return result.inserted_id

    # ============================================================
    # Check whether an admin already exists
    # ============================================================

    def exists(self):
        return self.collection.count_documents({}, limit=1) > 0