# models/admin.py

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class Admin(BaseModel):
    """
    Admin model used for authentication.

    The password field stores the HASHED password only.
    Never store a plain-text password in the database.
    """

    id: Optional[str] = Field(default=None, alias="_id")

    username: str
    email: EmailStr

    password_hash: str

    role: str = "admin"

    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True