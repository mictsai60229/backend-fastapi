from pydantic import BaseModel, validator

class SentimentRequest(BaseModel):
    sent: str
    language: str

    @validator('*')
    def not_empty(cls, v):
        if not v:
            raise ValueError("Value is required")
        return v
    
    @validator('language')
    def in_languages(cls, v):
        if v not in {"en", "zh-tw"}:
            raise ValueError("Language is not support")
        return v

class Sentiment(BaseModel):
    sentiment: str
    probability: float

class Metadata(BaseModel):
    status: str = "0000"
    desc: str = "Sucess"

class SentimentResponse(BaseModel):
    metadata: Metadata = Metadata()
    data: Sentiment