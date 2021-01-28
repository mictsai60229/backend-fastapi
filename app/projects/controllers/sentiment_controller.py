from app.projects.models import response, request


def get(sent: request.Sent):
    data = {"sentiment": "positive", "probability": "99.7"}
    sentiment_response = response.SentimentResponse(data=data)
    return sentiment_response