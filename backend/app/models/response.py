from typing import Dict, Optional
from pydantic import BaseModel

from backend.app.models.common import Sentiment


class Metadata(BaseModel):
    status: str = "0000"
    desc: str = "Sucess"

    
class BaseResponse(BaseModel):
    metadata: Metadata = Metadata()
    data: Optional[Dict] = None

class SentimentResponse(BaseResponse):
    data: Sentiment


