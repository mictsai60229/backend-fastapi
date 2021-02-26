from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi import Request, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from config.response import STATUS
from backend.logging.helpers import log_exception

# custom error usage
async def http_exception_handler(request: Request, excpetion: HTTPException) -> JSONResponse:
    headers = getattr(excpetion, "headers", None)
    metadata = getattr(excpetion, "metadata", None)
    metadata = metadata or {'status': '9999', 'desc': STATUS['9999']}
    data = getattr(excpetion, "data", None)
    
    if headers:
        return JSONResponse(
            {"metadata": metadata, "data": data}, status_code=excpetion.status_code, headers=headers
        )
    else:
        return JSONResponse({"metadata": metadata, "data": data}, status_code=excpetion.status_code)

# validation error
async def request_validation_exception_handler(
        request: Request, excpection: RequestValidationError
    ) -> JSONResponse:
    metadata = {"status": "1000", "desc":jsonable_encoder(excpection.errors())}
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"metadata": metadata, "data": None, },
    )

# server error
async def internal_server_error_handler(
        request: Request, excpection
    ) -> JSONResponse:
    metadata = {'status': '9999', 'desc': STATUS['9999']}
    await log_exception(request, excpection)
    return JSONResponse({"metadata": metadata, "data": None}, status_code=500)

HANDLERS = {HTTPException: http_exception_handler,
            RequestValidationError: request_validation_exception_handler,
            500: internal_server_error_handler}