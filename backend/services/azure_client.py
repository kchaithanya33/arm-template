from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient


subscription_id = "cc65e704-15de-4ddc-aa64-56973ac617f8"


def get_resource_groups():

    credential = AzureCliCredential()

    client = ResourceManagementClient(
        credential,
        subscription_id
    )

    resource_groups = []

    for rg in client.resource_groups.list():

        resource_groups.append(
            {
                "name": rg.name,
                "location": rg.location
            }
        )

    return resource_groups