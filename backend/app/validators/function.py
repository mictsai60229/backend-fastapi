from typing import Any
from pydantic import ValidationError



def not_empty(v: Any):
    if not v:
        raise ValueError('empty')
    return v


def value_in(collection: Any):

    def wrapper(v: Any):
        if v not in collection:
            raise ValueError('not in specific type')
        return v
    return wrapper
