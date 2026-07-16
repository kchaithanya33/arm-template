from app.deployment.schemas import DeploymentRequest
from app.deployment.parameter_generator import generate_parameters


request = DeploymentRequest(

    resourceGroup="arm-functionapp-test-rg",

    location="Central India",

    storageAccountName="mystorage123",

    applicationInsightsName="my-ai",

    appServicePlanName="my-plan",

    functionAppName="my-function",

    logicAppName="my-logic"
)


parameters = generate_parameters(request)

print(parameters)