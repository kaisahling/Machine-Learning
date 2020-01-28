def pred(request):
    from google.cloud import storage
    import joblib
    import sklearn
    import pandas as pd 
    import pickle as pk
    from flask import jsonify
    data = {"success": False}
    params = request.get_json()
    if "G1" in params: 
        
        param = params.get("G1")
        
        # set up access to the GCS bucket 
        bucket_name = "model_store_cloud_api_demo"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        # download and load the model
        blob = bucket.blob("serverless/constant/v1")
        blob.download_to_filename("/tmp/constant.pkl")

        model = pk.load( open("/tmp/constant.pkl", 'rb') )
        prediction = model.predict([param])[0]
        data["response"] = prediction
        #data["response"] = 1
        data["success"] = True
    
    return jsonify(data)
