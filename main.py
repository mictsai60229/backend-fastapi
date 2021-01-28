from fastapi import FastAPI

from app.routes import router
from config.base import settings, Settings

app = FastAPI()

app.include_router(router)


@app.get("/")
async def hello(settings: Settings = settings):
    return {
        "app_name": settings.app_name
    }

