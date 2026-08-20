# services/admin_service.py

from pwdlib import PasswordHash

from repositories.admin_repository import AdminRepository


class AdminService:

    def __init__(self):

        self.admin_repository = AdminRepository()

        self.password_hash = PasswordHash.recommended()

    # =========================================================
    # ADMIN LOGIN
    # =========================================================

    def authenticate_admin(
        self,
        login: str,
        password: str
    ):

        # Find admin using username OR email
        admin = self.admin_repository.find_by_username_or_email(
            login
        )

        # Admin does not exist
        if not admin:
            return None

        # Get stored password hash
        stored_password_hash = admin.get(
            "password_hash"
        )

        if not stored_password_hash:
            return None

        # Verify password
        try:

            password_valid = self.password_hash.verify(
                password,
                stored_password_hash
            )

        except Exception:

            return None

        # Invalid password
        if not password_valid:
            return None

        # Authentication successful
        return admin

    # =========================================================
    # GET ADMIN BY ID
    # =========================================================

    def get_admin_by_id(
        self,
        admin_id: str
    ):

        return self.admin_repository.find_by_id(
            admin_id
        )