import joblib
import pickle as pk
import numpy as np
from sklearn.dummy import DummyClassifier
import os



PATH = os.path.dirname(os.path.abspath(__file__))

CONSTANT = 0.42

def build_model():
    clf = DummyClassifier(strategy="most_frequent")
    return clf

def train_model(x, y):
    
    model = build_model()
    model.fit(x, y)
    return model

def upload_model(bucket_name,uri,model_name):
    from google.cloud import storage
    storage_client = storage.Client()

    try:
        bucket = storage_client.get_bucket(bucket_name)
    except RuntimeError:
        storage_client.create_bucket(bucket_name)
        bucket = storage_client.get_bucket(bucket_name)

    blob = bucket.blob(uri)
    blob.upload_from_filename(model_name)

if __name__ == "__main__":
    x_train = np.array([-1, 1, 1, 1])
    y_train = np.array([0, 1, 1, 1])
    model = train_model(x_train, y_train)
    num_of_features = 10
    assert model.predict(np.random.rand(1, num_of_features))[0] == 1
    model_name = "constant.pkl"
    pk.dump( model, open( os.path.join(PATH, model_name), "wb" ) )
    #joblib.dump(model, os.path.join(PATH, model_name))
    upload_model("model_store_cloud_api_demo","serverless/constant/v1",model_name)
