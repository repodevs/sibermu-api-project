from pydantic import EmailStr
from sqlmodel import Field

from app.model.base import Base


class User(Base, table=True):
    email: EmailStr | None = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)
    hashed_password: str

