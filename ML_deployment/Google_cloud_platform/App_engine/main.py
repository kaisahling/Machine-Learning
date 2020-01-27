import os

import flask
import joblib

PATH = os.path.dirname(os.path.abspath(__file__))

app = flask.Flask(__name__)

model_fname = "constant.joblib"
app.my_model = joblib.load(os.path.join(PATH, f"models/{model_fname}"))


@app.route("/")
def info():
    return flask.jsonify({"model_instance": model_fname})


@app.route("/predict", methods=["POST"])
def predict():
    x = flask.request.args.get("feature_vector")

    prediction = app.my_model.predict([x])[0]

    result = {"prediction": prediction}

    return flask.jsonify({"model_instance": model_fname,
                          "result": result})


if __name__ == "__main__":
    app.run(debug=True)

