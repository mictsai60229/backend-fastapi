import logging
import json

from config.logging import settings
from pythonjsonlogger.jsonlogger import JsonFormatter


class CustomJsonFormatter(JsonFormatter):
    def parse(self):
        return self._fmt

def get_rotated_handaler():
    return logging.handlers.RotatingFileHandler(settings.log_file, maxBytes=settings.max_bytes, backupCount=settings.backup_count)

def set_request_logger():
    #create logger name fastapi.request
    logger = logging.getLogger('fastapi.request')
    logger.setLevel(logging.INFO)
    #create handler
    file_handler = get_rotated_handaler()
    file_handler.setLevel(logging.INFO)
    #create formatter
    request_fields = ['system', 'request', 'trace_info', 'log_label', 'datatime', 'message']
    json_formatter = CustomJsonFormatter(request_fields, json_encoder=json.JSONEncoder)
    file_handler.setFormatter(json_formatter)
    # add handler to logger
    logger.addHandler(file_handler)

    
    return logger

def set_response_logger():
    #create logger name fastapi.response
    logger = logging.getLogger('fastapi.response')
    logger.setLevel(logging.INFO)
    #create handler
    file_handler = get_rotated_handaler()
    file_handler.setLevel(logging.INFO)
    #create formatter
    request_fields = ['system', 'request', 'response', 'trace_info', 'log_label', 'datatime', 'message']
    json_formatter = CustomJsonFormatter(request_fields, json_encoder=json.JSONEncoder)
    file_handler.setFormatter(json_formatter)
    # add handler to logger
    logger.addHandler(file_handler)

def set_expection_logger():
    #create logger name fastapi.expection
    logger = logging.getLogger('fastapi.expection')
    logger.setLevel(logging.INFO)
    #create handler
    file_handler = get_rotated_handaler()
    file_handler.setLevel(logging.INFO)
    #create formatter
    request_fields = ['system', 'request', 'trace_info', 'expection_info', 'log_label', 'datatime', 'message']
    json_formatter = CustomJsonFormatter(request_fields, json_encoder=json.JSONEncoder)
    file_handler.setFormatter(json_formatter)
    # add handler to logger
    logger.addHandler(file_handler)

def get_loggers():
    set_request_logger()
    set_response_logger()
    set_expection_logger()


LOGGERS = {
    'request' : logging.getLogger('fastapi.request'),
    'response' : logging.getLogger('fastapi.response'),
    'expection' : logging.getLogger('fastapi.expection')
}

