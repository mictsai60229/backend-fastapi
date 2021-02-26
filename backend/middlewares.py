import uuid

from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class HandleRequestUuidMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if 'request_uuid' in request.headers:
            request.state.request_uuid = request.headers['request_uuid']
        else:
            request.state.request_uuid = str(uuid.uuid4())
        response = await call_next(request)
        return response