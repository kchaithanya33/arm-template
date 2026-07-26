from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.core.exceptions import HttpResponseError
from app.services.azure_clients import (
    get_resource_client
)



# ======================================================
# RESOURCE GROUP OPERATIONS
# ======================================================


# ------------------------------------------------------
# Get all Resource Groups in Subscription
# ------------------------------------------------------

def get_resource_groups(subscription_id):


    client = get_resource_client(
        subscription_id
    )


    resource_groups = []


    for rg in client.resource_groups.list():


        resource_groups.append({

            "name": rg.name,

            "location": rg.location,

            "id": rg.id

        })


    return resource_groups


def get_locations(subscription_id: str):

    credential = DefaultAzureCredential()

    subscription_client = SubscriptionClient(
        credential
    )

    locations = []

    for location in subscription_client.subscriptions.list_locations(
        subscription_id
    ):

        locations.append(
            {
                "name": location.name,
                "display_name": location.display_name
            }
        )

    return locations
# ======================================================
# VALIDATE RESOURCE GROUP ACCESS
# ======================================================

def validate_resource_group_access(

        subscription_id,

        resource_group_name

):


    client = get_resource_client(
        subscription_id
    )


    try:


        rg = client.resource_groups.get(

            resource_group_name

        )


        return {


            "allowed": True,


            "name": rg.name,


            "location": rg.location,


            "id": rg.id

        }




    except HttpResponseError as e:



        if e.status_code == 403:


            return {


                "allowed": False,


                "error": "ACCESS_DENIED",


                "message": str(e)

            }



        elif e.status_code == 404:


            return {


                "allowed": False,


                "error": "NOT_FOUND",


                "message": str(e)

            }



        raise e