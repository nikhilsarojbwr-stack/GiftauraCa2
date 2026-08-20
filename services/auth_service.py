from datetime import datetime

from pwdlib import PasswordHash

from models.user import User
from repositories.user_repository import UserRepository

print("Loading AuthService from:")
print(__file__)
class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()
        self.password_hasher = PasswordHash.recommended()

    # =====================================================
    # Register User
    # =====================================================

    def register_user(self, user: User):

        # Check if email already exists
        existing_user = self.user_repository.find_by_email(user.email)

        if existing_user:
            return {
                "success": False,
                "message": "Email already registered."
            }

        # Hash Password
        hashed_password = self.password_hasher.hash(user.password)

        # Prepare User Document
        user_data = {
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "password": hashed_password,
            "role": user.role,
            "is_verified": user.is_verified,
            "is_active": user.is_active,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        # Save User
        user_id = self.user_repository.register_user(user_data)

        return {
            "success": True,
            "message": "Registration Successful",
            "user_id": user_id
        }

    # =====================================================
    # Login User
    # =====================================================

    def login_user(self, email: str, password: str):

        user = self.user_repository.find_by_email(email)

        if not user:
            return {
                "success": False,
                "message": "Invalid Email or Password"
            }

        # Verify Password
        if not self.password_hasher.verify(password, user["password"]):
            return {
                "success": False,
                "message": "Invalid Email or Password"
            }

        if not user.get("is_active", True):
            return {
                "success": False,
                "message": "Account Disabled"
            }

        return {
            "success": True,
            "message": "Login Successful",
            "user": user
        }

    # =====================================================
    # Get User
    # =====================================================

    def get_user_by_email(self, email: str):

        return self.user_repository.find_by_email(email)

    def get_user_by_id(self, user_id: str):

        return self.user_repository.find_by_id(user_id)

    def get_all_users(self):

        return self.user_repository.get_all_users()

    # =====================================================
    # Update User
    # =====================================================

    def update_user(self, user_id: str, update_data: dict):

        update_data["updated_at"] = datetime.utcnow()

        return self.user_repository.update_user(
            user_id,
            update_data
        )

    # =====================================================
    # Delete User
    # =====================================================

    def delete_user(self, user_id: str):

        return self.user_repository.delete_user(user_id)