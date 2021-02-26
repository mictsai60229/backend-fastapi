import logging
import json
import uuid
import time
from typing import Any
import traceback
import sys

from fastapi import Request, Response

from backend.logging.formatters import RequestData, SystemInfomation, BaseTraceInformation, RequestLogFormatter
from backend.logging.formatters import ResponseRequestData, ResponseData, ResponseLogFormatter
from backend.logging.formatters import ExceptionRequestData, ExceptionTraceInformation, ExceptionInformation, ExceptionLogFormatter
from backend.logging.loggers import LOGGERS

async def log_request(request: Request) -> RequestLogFormatter:
    
    body = await request.json()
    request_data = RequestData(
        headers = json.dumps({key:value for key, value in request.headers.items()}),
        ip = str(request.client.host),
        url = str(request.url),
        host = request.url.hostname,
        method = request.method,
        uuid = request.state.request_uuid,
        body = json.dumps(body),
        route = request['path'],
    )
    system_information = SystemInfomation()
    trace_information = BaseTraceInformation(
        run_time = int((time.time()-request.state.time_started)*1000)
    )
    message = "log_request: {route}".format(route=request_data.route)

    request_log = RequestLogFormatter(
        message = message,
        system = system_information,
        request = request_data,
        trace_info = trace_information
    )

    LOGGERS['request'].info(request_log.dict())

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

    request_data = ResponseRequestData(
        method = request_log.request.method,
        route = request_log.request.route,
        ip = request_log.request.ip,
        uuid = request_log.request.uuid
    )
    
    system_information = SystemInfomation()
    trace_information = BaseTraceInformation(
        run_time = int((time.time()-request.state.time_started)*1000)
    )
    message = "log_response: {route}".format(route=request_log.request.route)

    response_log = ResponseLogFormatter(
        message = message,
        system = system_information,
        request = request_data,
        response = response_data,
        trace_info = trace_information
    )

    LOGGERS['response'].info(response_log.dict())

    return response_log


async def log_exception(request: Request, exception: Any) -> None:

    # extract log data
    exception_type, message, exception_stack = sys.exc_info()
    tarcebacks = traceback.extract_tb(exception_stack)
    last_call_stack = tarcebacks[-1]
    filename = last_call_stack[0] 
    line_number = last_call_stack[1] 
    functin_name = last_call_stack[2]

    request_data = ExceptionRequestData(
        uuid = request.state.request_uuid
    )
    system_information = SystemInfomation(
        level = "error"
    )

    trace_infomation = ExceptionTraceInformation(
        backtrace = traceback.format_exc(),
        file = last_call_stack[0],
        function = last_call_stack[2],
        line = last_call_stack[1],
        run_time = int((time.time()-request.state.time_started)*1000)
    )

    exception_infomation = ExceptionInformation(
        error_code = str(exception_type),
        message = str(message)
    )

    exception_log = ExceptionLogFormatter(
        message = str(message),
        system = system_information,
        request = request_data,
        trace_info = trace_infomation,
        excption_info = exception_infomation
    )

    LOGGERS['expection'].info(exception_log.dict())