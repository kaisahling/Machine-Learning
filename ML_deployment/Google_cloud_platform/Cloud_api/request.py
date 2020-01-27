import requests
import numpy as np

url = 'http://0.0.0.0:5001/prediction/v1/predict'
payload = {"feature_vector": np.random.rand(10).tolist()}
r = requests.post(url,json=payload)

print(r.json())