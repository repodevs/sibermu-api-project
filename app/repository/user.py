
from typing import Optional
from sqlmodel import Session

from app.core.utils import get_password_hash
from app.repository.base import RepositoryBase
from app.model.user import User
from app.dto.user import UserCreate


class RepositoryUser(RepositoryBase[User]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create_user(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User.model_validate(
            obj_in,
            update={"hashed_password": get_password_hash(obj_in.password)}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def create_superuser(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User.model_validate(
            obj_in,
            update={
                "hashed_password": get_password_hash(obj_in.password),
                "is_active": True,
                "is_superuser": True,
            }
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

user = RepositoryUser(User)
