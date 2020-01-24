import os

import flask
import joblib

PATH = os.path.dirname(os.path.abspath(__file__))

app = flask.Flask(__name__)

os.environ["MY_MODEL_FILE"] = "constant.joblib"
model_fname = os.environ["MY_MODEL_FILE"]
app.my_model = joblib.load(os.path.join(PATH, f"models/{model_fname}"))


@app.route("/info")
def info():
    return flask.jsonify({"model_instance": model_fname})


@app.route("/prediction/v1/predict", methods=["POST"])
def predict():
    x = flask.request.args.get("feature_vector")

    prediction = app.my_model.predict([x])[0]

    result = {"prediction": prediction}

    return flask.jsonify({"model_instance": model_fname,
                          "result": result})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001)

