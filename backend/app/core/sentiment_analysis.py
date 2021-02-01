from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

PREDICTOR = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/basic_stanford_sentiment_treebank-2020.06.09.tar.gz")

def predict(text):
    result = PREDICTOR.predict(text)
    return result_format(result)

def result_format(result):

    formatted_result = {}
    idx, probs = max(enumerate(result['probs']), key=lambda x: x[1])
    formatted_result['sentiment'] = str(idx)
    formatted_result['probability'] = probs
    
    return formatted_result

    

    
    


