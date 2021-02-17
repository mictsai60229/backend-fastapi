from typing import Callable
import time

from fastapi import Request, Response
from fastapi.routing import APIRoute
from fastapi import APIRouter, Depends

from backend.app.formatters.sentiment import SentimentResponse, SentimentRequest
from backend.app.controllers import sentiment_controller
from backend.logging.helpers import log_request, log_response

class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()
        
        async def logging_route_handler(request: Request) -> Response:
            request.state.time_started = time.time()
            request_log = await log_request(request)
            response = await original_route_handler(request)
            await log_response(request, response, request_log)
            return response
        
        return logging_route_handler


router = APIRouter(route_class=LoggingRoute)

@router.get("/get/sentiment", response_model=SentimentResponse)
async def get_sentiment(request: SentimentRequest):
    return sentiment_controller.get(request)