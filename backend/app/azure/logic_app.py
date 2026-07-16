from azure.mgmt.resource.resources import ResourceManagementClient

from app.azure.auth import get_credential, get_subscription_id


# Create Resource Management client
client = ResourceManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


def get_logic_apps():
    """
    Returns all Logic Apps in the current subscription.
    """

    logic_apps = []

    resources = client.resources.list(
        filter="resourceType eq 'Microsoft.Logic/workflows'"
    )

    for resource in resources:

        logic_apps.append(
            {
                "id": resource.id,
                "name": resource.name,
                "location": resource.location,
                "resource_group": resource.id.split("/")[4],
                "type": resource.type
            }
        )

    return logic_apps


