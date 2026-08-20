from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class User(BaseModel):
    """
    User Model
    """

    full_name: str = Field(..., min_length=3, max_length=100)

    email: EmailStr

    phone: str = Field(..., min_length=10, max_length=15)

    password: str

    role: str = "customer"

    is_verified: bool = False

    is_active: bool = True

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserLogin(BaseModel):
    """
    Login Model
    """

    email: EmailStr

    password: str


class UserResponse(BaseModel):
    """
    Safe User Response
    (Never return password)
    """

    id: Optional[str] = None

    full_name: str

    email: EmailStr

    phone: str

    role: str

    is_verified: bool

    is_active: bool

    created_at: datetime