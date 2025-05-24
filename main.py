from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.core.db import init_db
from app.core.config import settings
from app.route.main import api_router
from app.route.ui import router as ui_router


def on_startup():
    # This function can be used to perform any startup tasks
    # such as initializing the database or loading initial data.
    init_db()

def get_app() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        on_startup=[on_startup]
    )

    # application.mount("/static", StaticFiles(directory="app/static"), name="static")

    @application.get("/")
    async def index():
        # redirect to the UI
        return RedirectResponse(ui_router.prefix)

    # include the API router
    application.include_router(api_router, prefix=settings.API_V1_STR)
    application.include_router(ui_router)

    return application

app = get_app()
