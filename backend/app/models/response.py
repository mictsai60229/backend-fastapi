from typing import Dict, Optional
from pydantic import BaseModel


class Metadata(BaseModel):
    status: str = "0000"
    desc: str = "Sucess"

    
class BaseResponse(BaseModel):
    metadata: Metadata = Metadata()
    data: Optional[Dict] = None


class Sentiment(BaseModel):
    sentiment: str
    probability: float

class SentimentResponse(BaseResponse):
    data: Sentiment


