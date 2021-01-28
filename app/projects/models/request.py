from pydantic import BaseModel


class Sent(BaseModel):
    sent: str
    language: str