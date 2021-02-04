from pydantic import BaseModel, validator

from backend.app.validators.function import not_empty, value_in
from backend.helpers import build_validator


class SentimentRequest(BaseModel):
    sent: str
    language: str
    
    #validators
    _not_empty_sent = build_validator('sent', func=not_empty)
    _in_languages = build_validator('language', func=value_in({"zh-tw", "en"}))

    @validator('sent')
    def sent_normalize(cls, v):
        return v.lower()
        

class Sentiment(BaseModel):
    sentiment: str
    probability: float

class Metadata(BaseModel):
    status: str = "0000"
    desc: str = "Sucess"

class SentimentResponse(BaseModel):
    metadata: Metadata = Metadata()
    data: Sentiment