import joblib
import numpy as np
from sklearn.dummy import DummyClassifier
import os


PATH = os.path.dirname(os.path.abspath(__file__))

CONSTANT = 0.42

def build_model():
    clf = DummyClassifier(strategy="constant", constant=CONSTANT)
    return clf


def train_model(x, y):
    model = build_model()
    print(x.shape, y.shape)
    model.fit(x, y)
    return model


if __name__ == "__main__":
    num_of_features = 10
    x_train = np.ones((1, num_of_features))
    y_train = np.full((1, ), CONSTANT)
    model = train_model(x_train, y_train)
    assert model.predict(np.random.rand(1, num_of_features))[0] == CONSTANT
    joblib.dump(model, os.path.join(PATH, "constant.joblib"))
    os.environ["MY_MODEL_FILE"] = os.path.join(PATH, "constant.joblib")
    print(os.environ["MY_MODEL_FILE"])
