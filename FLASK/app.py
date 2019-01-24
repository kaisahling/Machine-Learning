from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from sklearn.svm import SVC

app = Flask(__name__)
api = Api(app)

svc = SVC()

svc_path = 'models/svm.pkl'
with open(svc_path, 'rb') as pkl:
    svc = pickle.load(pkl)


# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class PredictIris(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']

        data = np.reshape(np.array(user_query), (-1, 4))

        # vectorize the user's query and make a prediction
        prediction = svc.predict(data)
        pred_proba = svc.predict_proba(data)

        # Output either 'Negative' or 'Positive' along with the score
        if prediction == 'setosa':
            pred_text = 'Setosa'
        elif prediction == 'versicolor':
            pred_text = 'Versicolor'
        else: 
            pred_text = 'Virginica'

        # round the predict proba value and set to new variable
        confidence = round(pred_proba[0], 3)

        # create JSON object
        output = {'prediction': pred_text, 'confidence': confidence}

        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictIris, '/')


if __name__ == '__main__':
    app.run(debug=True)