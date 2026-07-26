from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.core.exceptions import HttpResponseError
from azure.mgmt.storage import StorageManagementClient
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
# ======================================================
# STORAGE ACCOUNT OPERATIONS
# ======================================================


# ------------------------------------------------------
# Get all Storage Accounts in Subscription
# ------------------------------------------------------

def get_storage_accounts(subscription_id):


    credential = DefaultAzureCredential()


    storage_client = StorageManagementClient(
        credential,
        subscription_id
    )


    storage_accounts = []


    for account in storage_client.storage_accounts.list():


        storage_accounts.append({

            "name": account.name,

            "location": account.location,

            "resource_group": account.id.split("/")[4],

            "id": account.id

        })


    return storage_accounts

# ------------------------------------------------------
# Validate Storage Account Access
# ------------------------------------------------------
def validate_storage_resource_group(
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
            "location": rg.location
        }


    except HttpResponseError as e:

        return {
            "allowed": False,
            "message": str(e)
        }
        
# ======================================================
# Validate Storage Account Access
# ======================================================

def validate_storage_account_access(
        subscription_id,
        resource_id
):


    credential = DefaultAzureCredential()


    storage_client = StorageManagementClient(
        credential,
        subscription_id
    )


    try:

        # Extract resource group and storage name
        # from resource ID

        parts = resource_id.split("/")

        resource_group_name = parts[4]

        storage_account_name = parts[-1]



        account = storage_client.storage_accounts.get_properties(

            resource_group_name,

            storage_account_name

        )


        return {

            "allowed": True,

            "name": account.name,

            "location": account.location,

            "id": account.id

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