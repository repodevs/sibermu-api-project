import uuid
from typing import Any, List

from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException

from app.core import deps
from app import dto
from app.repository.user import user as userRepo


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[dto.User])
async def lists(skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db)) -> List[dto.User]:    
    users = userRepo.get_multi(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=dto.User)
def create(
    user_in: dto.UserCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    user = userRepo.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = userRepo.create_user(db, obj_in=user_in)
    return user

@router.get("/{user_id}", response_model=dto.UserDetail)
def retrieve(
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    user = userRepo.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system.",
        )
    return user

@router.patch("/{user_id}", response_model=dto.UserUpdate)
def update(
    user_id: uuid.UUID,
    user_in: dto.UserUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    user = userRepo.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system.",
        )
    if user_in.email:
        existing_user = userRepo.get_by_email(db, email=user_in.email)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=400, detail="Email already registered"
            )
    user = userRepo.update(db, db_obj=user, obj_in=user_in)
    return user

@router.delete("/{user_id}")
def delete(
    user_id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    user = userRepo.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this id does not exist in the system.",
        )
    userRepo.remove(db, id=user_id)
    return {"ok": True}
