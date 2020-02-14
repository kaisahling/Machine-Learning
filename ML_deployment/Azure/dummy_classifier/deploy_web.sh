#!/bin/bash
az ml model deploy -n dummyclassifierwebservice -m dummyclassifier:1 --ic inferenceConfig.json --dc deploymentConfigWeb.json -w Demo -g Demo --overwrite