from pydantic import BaseModel


class Sent(BaseModel):
    sent: str
    language: str


class Sentiment(BaseModel):
    sentiment: str
    probability: float