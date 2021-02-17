from fastapi import FastAPI

from backend.routes import router
from backend.exceptions.exception_handlers import HANDLERS
from backend.logging.loggers import get_loggers
from config.base import settings

get_loggers()

app = FastAPI(exception_handlers=HANDLERS)

app.include_router(router)


@app.get("/")
async def hello():
    return {
        "app_name": settings.app_name
    }

