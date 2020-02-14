Sample request to DummyClassifier when deployed to web:

```
curl -X POST \
  http://a7ebc567-c482-44f9-bb1b-bb4709168a4c.westeurope.azurecontainer.io/score
  -H 'Accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{"G1": [20,0.8,5,1000]}'
```

Response:
```
{
    "success": true,
    "response": [
        1,
        1,
        1,
        1
    ]
}
```