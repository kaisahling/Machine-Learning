import os
import pickle as pk
import json
from flask import jsonify

# Called when the deployed service starts
def init():
    global model
    # Get the path where the deployed model can be found.
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), './models')
    # load models
    model = pk.load(open(model_path + "/constant.pkl", 'rb'))


# Handle requests to the service
def run(data):
    result = {"success": False}
    try:
        data = json.loads(data)
        prediction = model.predict(data['G1'])
        result["success"] = True
        result["response"] = prediction.tolist()
        return result
    except Exception as e:
        result["error"] = str(e)
        return result
