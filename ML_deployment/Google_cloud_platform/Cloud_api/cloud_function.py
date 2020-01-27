def pred(request):
    from google.cloud import storage
    import joblib
    import sklearn
    import pandas as pd 
    from flask import jsonify
    data = {"success": False}
    params = request.get_json()
    if "G1" in params: 
        
        new_row = { "G1": params.get("G1"),"G2": params.get("G2"), 
                    "G3": params.get("G3"),"G4": params.get("G4"), 
                    "G5": params.get("G5"),"G6": params.get("G6"), 
                    "G7": params.get("G7"),"G8": params.get("G8"), 
                    "G9": params.get("G9"),"G10":params.get("G10")}
        x = pd.DataFrame.from_dict(new_row, 
                                      orient = "index").transpose()
        
        # set up access to the GCS bucket 
        bucket_name = "model_store_cloud_api_demo"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        # download and load the model
        blob = bucket.blob("serverless/constant/v1")
        blob.download_to_filename("/tmp/constant.joblib")
        model = pk.load(open("/tmp/constant.joblib", 'rb'))
     
        data["response"] = str(model.model.predict(x['G1'][0])[0])
        data["success"] = True
    
    return jsonify(data)
