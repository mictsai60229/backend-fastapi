import logging
import json
import uuid
import time

from fastapi import Request, Response

from backend.logging.formatters import RequestData, SystemInfomation, TraceInformation, RequestLogFormatter
from backend.logging.formatters import SimpleRequestData, ResponseData, ResponseLogFormatter


REQUEST_LOGGER = logging.getLogger('fastapi.request')
RESPONSE_LOGGER = logging.getLogger('fastapi.response')

async def log_request(request: Request) -> RequestLogFormatter:
    
    body = await request.json()
    request_data = RequestData(
        headers = json.dumps({key:value for key, value in request.headers.items()}),
        ip = str(request.client.host),
        url = str(request.url),
        host = request.url.hostname,
        method = request.method,
        uuid = request.headers.get('', None) or str(uuid.uuid4()),
        body = json.dumps(body),
        route = request['path'],
    )
    system_information = SystemInfomation()
    trace_information = TraceInformation(
        run_time = int((time.time()-request.state.time_started)*1000)
    )
    message = "log_request: {route}".format(route=request_data.route)

    request_log = RequestLogFormatter(
        message = message,
        system = system_information,
        request = request_data,
        trace_info = trace_information
    )

    REQUEST_LOGGER.info(request_log.dict())

    return request_log

async def log_response(request: Request, response: Response, request_log: RequestLogFormatter) -> ResponseLogFormatter:

    body = response.body.decode("utf-8")
    metadata = json.loads(body).get('metadata', {})
    response_data = ResponseData(
        http_status = str(response.status_code),
        body = response.body.decode("utf-8"),
        headers = json.dumps({key:value for key, value in response.headers.items()}),
        meta_status = metadata.get("status", ""),
        meta_description = metadata.get("desc", None)
    )

    simple_request_data = SimpleRequestData(
        method = request_log.request.method,
        route = request_log.request.route,
        ip = request_log.request.ip,
        uuid = request_log.request.uuid
    )
    
    system_information = SystemInfomation()
    trace_information = TraceInformation(
        run_time = int((time.time()-request.state.time_started)*1000)
    )
    message = "log_response: {route}".format(route=request_log.request.route)

    response_log = ResponseLogFormatter(
        message = message,
        system = system_information,
        request = simple_request_data,
        response = response_data,
        trace_info = trace_information
    )

    RESPONSE_LOGGER.info(response_log.dict())

    return response_log