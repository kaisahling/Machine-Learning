#!/bin/bash
az ml model deploy -n dummyclassifierservice -m dummyclassifier:1 --ic inferenceConfig.json --dc deploymentConfig.json -w Demo -g Demo --overwrite