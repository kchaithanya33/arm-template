from azure.mgmt.resource import ResourceManagementClient

from app.services.azure_auth import get_credential



def delete_resource(
        subscription_id,
        resource_group,
        resource_name,
        resource_type
):


    credential=get_credential()


    client=ResourceManagementClient(
        credential,
        subscription_id
    )


    resource_id = (
        f"/subscriptions/{subscription_id}"
        f"/resourceGroups/{resource_group}"
        f"/providers/{resource_type}"
        f"/{resource_name}"
    )


    poller = client.resources.begin_delete_by_id(
        resource_id,
        "2023-07-01"
    )


    poller.result()



    return {

        "status":"success",

        "message":
        f"{resource_name} deleted successfully"

    }