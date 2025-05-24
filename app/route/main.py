from fastapi import APIRouter

from .user import router as user_router
from .integration import router as integration_router


api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(integration_router)
