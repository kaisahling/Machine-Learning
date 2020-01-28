import requests
import numpy as np

result = requests.post(
        "https://us-central1-cloud-api-demo-266422.cloudfunctions.net/function-dummy-clf"
         ,json = { 'G1':np.random.rand()})
print(result.json())
