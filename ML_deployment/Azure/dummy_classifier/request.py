import requests
import json
import numpy as np

# Scoring uri is displayed after deploying the model
scoring_uri = 'http://58f79881-f98d-4608-869b-76d3072cf717.westeurope.azurecontainer.io/score'
headers = {'Content-Type':'application/json'}

test_data = json.dumps({"G1": [20,0.8,5,1000]})

response = requests.post(scoring_uri, data=test_data, headers=headers)
print(response.status_code)
print(response.elapsed)
print(response.json())