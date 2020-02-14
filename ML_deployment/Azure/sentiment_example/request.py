import requests
import json
import numpy as np

# Scoring uri is displayed after deploying the model
scoring_uri = 'http://localhost:32773/score'
headers = {'Content-Type':'application/json'}

text = ['Today is a great day!','Today is a bad day!', 'I feel ok']

random_number = np.random.randint(3)
test_data = json.dumps({'text': text[random_number]})

response = requests.post(scoring_uri, data=test_data, headers=headers)
print(response.status_code)
print(response.elapsed)
print(response.json())