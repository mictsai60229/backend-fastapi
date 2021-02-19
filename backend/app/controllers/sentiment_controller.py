from backend.app.core.sentiment_analysis import predict
from backend.app.formatters.sentiment import SentimentResponse, SentimentRequest

def get(request: SentimentRequest)->SentimentResponse:

    result = predict(request.sent)
    sentiment_response = SentimentResponse(data=result)

    return sentiment_response
