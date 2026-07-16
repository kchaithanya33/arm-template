from azure.mgmt.resource.resources import ResourceManagementClient

from app.azure.auth import get_credential, get_subscription_id


# Create Azure Resource Management client
client = ResourceManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


def get_resource_groups():
    """
    Returns all Resource Groups in the current subscription.
    """

    resource_groups = []

    for rg in client.resource_groups.list():

        resource_groups.append(
            {
                "id": rg.id,
                "name": rg.name,
                "location": rg.location
            }
        )

    return resource_groups


