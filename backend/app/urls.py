from fastapi import APIRouter, Depends

from backend.app.formatters.sentiment import SentimentResponse, SentimentRequest
from backend.app.controllers import sentiment_controller

router = APIRouter()

@router.get("/get/sentiment", response_model=SentimentResponse)
async def get_sentiment(request: SentimentRequest):
    return sentiment_controller.get(request)