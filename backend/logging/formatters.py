from datetime import datetime
from typing import List, Optional
import os

from pydantic import BaseModel
from config import base

class RequestData(BaseModel):
    headers: str
    ip: str
    url: str
    host: str
    method: str
    uuid: str
    body: str
    route: str
    
class SystemInfomation(BaseModel):
    service_name: str = base.settings.service_name
    pid: int = os.getpid()
    level: str = "info"
    env: str = base.settings.env


class TraceInformation(BaseModel):
    run_time: int

class SimpleRequestData(BaseModel):
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


class RequestLogFormatter(BaseModel):
    message: str
    system: SystemInfomation
    request: RequestData
    trace_info : TraceInformation
    log_label: str  = "REQUEST"
    data_time: str = str(datetime.now())



class ResponseLogFormatter(BaseModel):
    message: str
    system: SystemInfomation
    request: SimpleRequestData
    response: ResponseData
    trace_info : TraceInformation
    log_label: str  = "RESPONSE"
    data_time: str = str(datetime.now())
    
