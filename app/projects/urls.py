from fastapi import APIRouter, Depends

from app.projects.models import response, request
from app.projects.controllers import sentiment_controller

router = APIRouter()

@router.get("/get/sentiment", response_model=response.SentimentResponse)
async def get_sentiment(sent: request.Sent):
    return sentiment_controller.get(sent)