import logging
import json

from config.logging import settings
from pythonjsonlogger.jsonlogger import JsonFormatter


class CustomJsonFormatter(JsonFormatter):
    def parse(self):
        return self._fmt

def _set_request_logger():
    #create logger name fastapi.request
    logger = logging.getLogger('fastapi.request')
    logger.setLevel(logging.INFO)
    #create handler
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setLevel(logging.INFO)
    #create formatter
    request_fields = ['system', 'request', 'trace_info', 'log_label', 'datatime', 'message']
    json_formatter = CustomJsonFormatter(request_fields, json_encoder=json.JSONEncoder)
    file_handler.setFormatter(json_formatter)
    # add handler to logger
    logger.addHandler(file_handler)

    
    return logger

def _set_response_logger():
     #create logger name fastapi.response
    logger = logging.getLogger('fastapi.response')
    logger.setLevel(logging.INFO)
    #create handler
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setLevel(logging.INFO)
    #create formatter
    request_fields = ['system', 'request', 'response', 'trace_info', 'log_label', 'datatime', 'message']
    json_formatter = CustomJsonFormatter(request_fields, json_encoder=json.JSONEncoder)
    file_handler.setFormatter(json_formatter)
    # add handler to logger
    logger.addHandler(file_handler)


def get_loggers():
    _set_request_logger()
    _set_response_logger()


