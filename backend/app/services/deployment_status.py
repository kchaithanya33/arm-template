from azure.mgmt.resource import ResourceManagementClient

from app.services.azure_auth import (
    get_credential,
    get_subscription_id
)


# ======================================================
# Get ARM Deployment Status
# ======================================================

def get_deployment_status(
        resource_group_name: str,
        deployment_name: str
):

    credential = get_credential()

    subscription_id = get_subscription_id()


    client = ResourceManagementClient(
        credential,
        subscription_id
    )


    deployment = client.deployments.get(
        resource_group_name,
        deployment_name
    )


    return {

        "deployment_name":
        deployment.name,


        "status":
        deployment.properties.provisioning_state,


        "timestamp":
        deployment.properties.timestamp

    }