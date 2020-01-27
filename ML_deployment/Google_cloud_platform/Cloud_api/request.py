import requests
import numpy as np

result = requests.post(
        "https://us-central1-gameanalytics.cloudfunctions.net/pred"
         ,json = { 'G1':np.random.rand(10).tolist(), 'G2':'0', 'G3':'0', 'G4':'0', 'G5':'0'
               ,'G6':'0', 'G7':'0', 'G8':'0', 'G9':'0', 'G10':'0'})
print(result.json())
