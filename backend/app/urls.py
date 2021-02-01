from fastapi import APIRouter, Depends

from backend.app.models.common import Sent
from backend.app.models.response import SentimentResponse
from backend.app.controllers import sentiment_controller

router = APIRouter()

@router.get("/get/sentiment", response_model=SentimentResponse)
async def get_sentiment(sent: Sent):
    return sentiment_controller.get(sent)