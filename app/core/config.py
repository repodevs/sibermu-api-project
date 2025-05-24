from typing import List, Optional, Union

from pydantic import EmailStr
from pydantic_settings import BaseSettings
from pydantic.class_validators import validator
from pydantic.networks import AnyHttpUrl, AnyUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "API Application"
    PROJECT_DESCRIPTION: str = "API Application for various purposes"

    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DEBUG: bool = False

    FIRST_SUPERUSER_EMAIL: EmailStr = "admin@example.com"
    FIRST_SUPERUSER_NAME: str = "Admin User"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQLALCHEMY_DATABASE_URI: Optional[AnyUrl] = None

    class Config:
        case_sensitive = True
        # dotenv
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
