from fastapi import FastAPI

from backend.routes import router
from backend.exceptions.exception_handlers import HANDLERS
from config.base import settings

app = FastAPI(exception_handlers=HANDLERS)

app.include_router(router)


@app.get("/")
async def hello():
    return {
        "app_name": settings.app_name
    }

