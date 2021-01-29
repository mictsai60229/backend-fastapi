from fastapi import APIRouter, Depends

from backend.app.models import response, request
from backend.app.controllers import sentiment_controller

router = APIRouter()

@router.get("/get/sentiment", response_model=response.SentimentResponse)
async def get_sentiment(sent: request.Sent):
    return sentiment_controller.get(sent)