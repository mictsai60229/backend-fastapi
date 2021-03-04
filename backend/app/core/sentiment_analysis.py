import random

def predict(text):
    return fake_predict()

def fake_predict():

    formatted_result = {}
    formatted_result['sentiment'] = str(random.randint(0,1))
    formatted_result['probability'] = random.uniform(0.5, 1.0)
    
    return formatted_result

    

    
    


