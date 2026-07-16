def generate_parameters(request):

    return {

        "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",

        "contentVersion": "1.0.0.0",

        "parameters": {

            "storageAccountName": {
                "value": request.storageAccountName
            },

            "applicationInsightsName": {
                "value": request.applicationInsightsName
            },

            "appServicePlanName": {
                "value": request.appServicePlanName
            },

            "functionAppName": {
                "value": request.functionAppName
            },

            "logicAppName": {
                "value": request.logicAppName
            },

            "location": {
                "value": request.location
            }

        }

    }