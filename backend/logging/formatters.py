from datetime import datetime
from typing import List, Optional
import os

from pydantic import BaseModel
from config import base

class SystemInfomation(BaseModel):
    service_name: str = base.settings.service_name
    pid: int = os.getpid()
    level: str = "info"
    env: str = base.settings.env

class BaseTraceInformation(BaseModel):
    run_time: int

class RequestData(BaseModel):
    headers: str
    ip: str
    url: str
    host: str
    method: str
    uuid: str
    body: str
    route: str

class ResponseRequestData(BaseModel):
    method: str
    route: str
    ip: str
    uuid : str

class ResponseData(BaseModel):
    http_status: str
    body: str
    headers: str
    meta_status: str
    meta_description: Optional[str]

class ExceptionRequestData(BaseModel):
    uuid : str

class ExceptionTraceInformation(BaseModel):
    backtrace: str
    file: str
    function: str
    line: str
    run_time: str

class ExceptionInformation(BaseModel):
    error_code: str
    message: str


class RequestLogFormatter(BaseModel):
    message: str
    system: SystemInfomation
    request: RequestData
    trace_info : BaseTraceInformation
    log_label: str  = "REQUEST"
    data_time: str = str(datetime.now())


class ResponseLogFormatter(BaseModel):
    message: str
    system: SystemInfomation
    request: ResponseRequestData
    response: ResponseData
    trace_info : BaseTraceInformation
    log_label: str  = "RESPONSE"
    data_time: str = str(datetime.now())

class ExceptionLogFormatter(BaseModel):
    message: str
    system : SystemInfomation
    request: ExceptionRequestData
    trace_info: ExceptionTraceInformation
    excption_info: ExceptionInformation
    log_label: str  = "EXCEPTION"
    data_time: str = str(datetime.now())
    
