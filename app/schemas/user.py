from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    interests: str
    role: UserRole

    class Config:
        from_attributes = True

class UpdateInterests(BaseModel):
    interests: str

class Token(BaseModel):
    access_token: str
    token_type: str