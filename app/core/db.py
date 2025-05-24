from sqlmodel import SQLModel, create_engine, Session, select

from app.core.config import settings
from app.model.user import User
from app.dto.user import UserCreate
from app.repository.user import user as userRepo


engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), pool_pre_ping=True, echo=settings.DEBUG)


def init_data(session: Session) -> None:
    # Generate the database tables
    SQLModel.metadata.create_all(engine)
    
    # init user
    init_user(session)


def init_user(session: Session) -> None:
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER_EMAIL)
    ).first()
    if not user:
        user_in = UserCreate(
            full_name=settings.FIRST_SUPERUSER_NAME,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
        )
        user = userRepo.create_superuser(db=session, obj_in=user_in)


def init_db() -> None:
    with Session(engine) as session:
        init_data(session)
