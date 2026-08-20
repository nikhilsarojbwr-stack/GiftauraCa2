from bson import ObjectId

from database.connection import db


class UserRepository:
    """
    Handles all MongoDB operations for users.
    """

    def __init__(self):
        self.collection = db["users"]

    # ----------------------------
    # Create
    # ----------------------------
    def register_user(self, user_data: dict):
        """
        Insert a new user.
        """
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    # ----------------------------
    # Read
    # ----------------------------
    def find_by_email(self, email: str):
        """
        Find user by email.
        """
        return self.collection.find_one({"email": email})

    def find_by_id(self, user_id: str):
        """
        Find user by ObjectId.
        """
        return self.collection.find_one(
            {"_id": ObjectId(user_id)}
        )

    def get_all_users(self):
        """
        Return all users.
        """
        return list(self.collection.find())

    # ----------------------------
    # Update
    # ----------------------------
    def update_user(self, user_id: str, update_data: dict):
        """
        Update user information.
        """
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        return result.modified_count

    # ----------------------------
    # Delete
    # ----------------------------
    def delete_user(self, user_id: str):
        """
        Delete a user.
        """
        result = self.collection.delete_one(
            {"_id": ObjectId(user_id)}
        )

        return result.deleted_count