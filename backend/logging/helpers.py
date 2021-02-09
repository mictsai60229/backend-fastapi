import logging
import json
import uuid
import time
from fastapi import Request

# Request
from backend.logging.formatters import RequestData, SystemInfomation, TraceInformation, RequestFormat


REQUEST_LOGGER = logging.getLogger('fastapi.request')

async def log_request(request: Request) -> None:
    
    data = await request.json()
    request_data = RequestData(
        headers = json.dumps({key:value for key, value in request.headers.items()}),
        ip = str(request.client.host),
        url = str(request.url),
        host = request.url.hostname,
        method = request.method,
        uuid = request.headers.get('', None) or str(uuid.uuid4()),
        body = json.dumps(data),
        route = request['path'],
    )
    system_information = SystemInfomation()
    trace_information = TraceInformation(
        run_time = int((time.time()-request.state.time_started)*1000)
    )
    message = "log request: {route}".format(route=request_data.route)

    request_format = RequestFormat(
        message = message,
        system = system_information,
        request = request_data,
        trace_info = trace_information
    )

    REQUEST_LOGGER.info(request_format.dict())