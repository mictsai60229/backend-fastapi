from backend.app.core.sentiment_analysis import predict
from backend.app.models.common import Sent
from backend.app.models.response import SentimentResponse

def get(sent: Sent):

    result = predict(sent.sent)

    sentiment_response = SentimentResponse(data=result)
    return sentiment_response
