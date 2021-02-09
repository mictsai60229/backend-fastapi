from fastapi import APIRouter, Depends
import logging
from typing import Callable
import time

from fastapi import Request, Response
from fastapi.routing import APIRoute
from backend.app.formatters.sentiment import SentimentResponse, SentimentRequest
from backend.app.controllers import sentiment_controller
from backend.logging.helpers import log_request

class CustomRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()
        
        async def custom_route_handler(request: Request) -> Response:
            request.state.time_started = time.time()
            await log_request(request)
            response = await original_route_handler(request)
            return response
        
        return custom_route_handler


router = APIRouter(route_class=CustomRoute)

@router.get("/get/sentiment", response_model=SentimentResponse)
async def get_sentiment(request: SentimentRequest):
    return sentiment_controller.get(request)