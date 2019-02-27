from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle, json
import numpy as np
import pandas as pd
from sklearn.svm import SVC

app = Flask(__name__)

svc = SVC()


@app.route("/form", methods=['POST'])
def predict_form():
    if request.method == 'POST':
        try:
            data = [] 
            data.append(request.form['Sepal_length'])
            data.append(request.form['Sepal_width'])
            data.append(request.form['Petal_length'])
            data.append(request.form['Petal_width'])
           
            #flower = []
            #for i in ['Sepal', 'Petal']:
            #    for j in ['Length', 'Width']: 
            #        flower.append(data.loc[j][i])

            # 
            prediction = svc.predict(data)
            pred_proba = svc.predict_proba(data)

            # 
            if prediction == 'setosa':
                pred_text = 'Setosa'
            elif prediction == 'versicolor':
                pred_text = 'Versicolor'
            else: 
                pred_text = 'Virginica'

            # round the predict proba value and set to new variable
            confidence = round(pred_proba[0], 3)

        except ValueError:
            return jsonify("Please submit a json file")

        return pred_text

@app.route("/param", methods=['GET'])
def predict_param():
    if request.method == 'GET':
        try:
            data = [] 
            data.append(request.args.get('Sepal_length', ''))
            data.append(request.args.get('Sepal_width', ''))
            data.append(request.args.get('Petal_length', ''))
            data.append(request.args.get('Petal_width', ''))
           
            #flower = []
            #for i in ['Sepal', 'Petal']:
            #    for j in ['Length', 'Width']: 
            #        flower.append(data.loc[j][i])

            # 
            prediction = svc.predict(data)
            pred_proba = svc.predict_proba(data)

            # 
            if prediction == 'setosa':
                pred_text = 'Setosa'
            elif prediction == 'versicolor':
                pred_text = 'Versicolor'
            else: 
                pred_text = 'Virginica'

            # round the predict proba value and set to new variable
            confidence = round(pred_proba[0], 3)

        except ValueError:
            return jsonify("Please submit a json file")

        return pred_text

@app.route("/json", methods=['POST'])
def predict_json():
    if request.method == 'POST':
        try:
            jsonfile = request.get_json()

            data = pd.read_json(jsonfile)

            flower = []
            for i in ['Sepal', 'Petal']:
                for j in ['Length', 'Width']: 
                    flower.append(data.loc[j][i])

            # 
            prediction = svc.predict(flower)
            pred_proba = svc.predict_proba(flower)

            # 
            if prediction == 'setosa':
                pred_text = 'Setosa'
            elif prediction == 'versicolor':
                pred_text = 'Versicolor'
            else: 
                pred_text = 'Virginica'

            # round the predict proba value and set to new variable
            confidence = round(pred_proba[0], 3)

        except ValueError:
            return jsonify("Please submit a json file")

        return pred_text

if __name__ == '__main__':

	modelfile = 'models/svm.pkl'   

	model = pickle.load(open(modelfile, 'rb'))

	print("loaded OK")

	app.run(debug=True)