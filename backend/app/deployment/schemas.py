from pydantic import BaseModel


class DeploymentRequest(BaseModel):

    resourceGroup: str

    location: str

    storageAccountName: str

    applicationInsightsName: str

    appServicePlanName: str

    functionAppName: str

    logicAppName: str