from typing import Callable
from pydantic import validator



def build_validator(*fields: str, func: Callable):
    return validator(*fields, allow_reuse=True)(func)