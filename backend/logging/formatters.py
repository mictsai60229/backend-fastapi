from datetime import datetime
from typing import List
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
    

class RequestFormat(BaseModel):
    message: str
    system: SystemInfomation
    request: RequestData
    trace_info : TraceInformation
    log_label: str  = "REQUEST"
    data_time: str = str(datetime.now())

    #fields: RequestFields
