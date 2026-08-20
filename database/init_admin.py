# database/init_admin.py

from datetime import datetime

from pwdlib import PasswordHash

from database.connection import db


# ============================================================
# ADMIN CREDENTIALS
# ============================================================

ADMIN_USERNAME = "admin"
ADMIN_EMAIL = "admin@giftaura.com"

# Change this to your desired password
ADMIN_PASSWORD = "gift@admin12"


# ============================================================
# PASSWORD HASHING
# ============================================================

password_hash = PasswordHash.recommended()


# ============================================================
# ADMIN COLLECTION
# ============================================================

admins_collection = db["admins"]


# ============================================================
# CHECK EXISTING ADMIN
# ============================================================

existing_admin = admins_collection.find_one({
    "$or": [
        {"username": ADMIN_USERNAME},
        {"email": ADMIN_EMAIL}
    ]
})


if existing_admin:

    print("⚠️ Admin account already exists.")

else:

    hashed_password = password_hash.hash(
        ADMIN_PASSWORD
    )

    admin_data = {
        "username": ADMIN_USERNAME,
        "email": ADMIN_EMAIL,
        "password_hash": hashed_password,
        "role": "admin",
        "created_at": datetime.utcnow()
    }

    result = admins_collection.insert_one(admin_data)

    print("✅ Admin account created successfully.")
    print(f"Username: {ADMIN_USERNAME}")
    print(f"Email: {ADMIN_EMAIL}")
    print("Password: [hidden]")
    print(f"Admin ID: {result.inserted_id}")