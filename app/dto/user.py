import uuid
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: uuid.UUID
    full_name: str
    email: EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None


class UserDetail(User):
    is_active: bool = True
    is_superuser: bool = False
