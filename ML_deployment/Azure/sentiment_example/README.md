How to use this example:

1. Run `register_model.sh` to register your model in Azure Machine Learning Workspace

2. Run `deploy_cli.sh` to deploy it. Deployment target (where do we deploy?) specified in `deploymentConfig.json`, deployed as web service runned in local Docker container by default.

In case you make changes to your model or the entry script, simply redeploy your model by running `deploy_cli.sh`. Make sure to enable overwriting in case you do not want to change the name of the model. The version change is tracked automatically. Note that the scoring uri changes with every deployment.
Pre-requirements:
1. Docker installed
2. Azure CLI installed and logged in
3. Machine Learning Workspace created 