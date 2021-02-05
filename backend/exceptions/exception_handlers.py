from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from config.response import STATUS


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    headers = getattr(exc, "headers", None)
    metadata = getattr(exc, "headers", None)
    metadata = metadata or {'status': '9999', 'desc': STATUS['9999']}
    
    if headers:
        return JSONResponse(
            {"metadata": metadata, "data": exc.data}, status_code=exc.status_code, headers=headers
        )
    else:
        return JSONResponse({"metadata": metadata, "data": exc.data}, status_code=exc.status_code)


async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    metadata = {"status": "1000", "desc":jsonable_encoder(exc.errors())}
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"metadata": metadata, "data": None, },
    )


HANDLERS = {HTTPException: http_exception_handler,
            RequestValidationError: request_validation_exception_handler}