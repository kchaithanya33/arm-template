from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.logic import LogicManagementClient


credential = DefaultAzureCredential()


# ======================================================
# Resource Client
# ======================================================

def get_resource_client(subscription_id):

    return ResourceManagementClient(
        credential,
        subscription_id
    )


# ======================================================
# Storage Client
# ======================================================

def get_storage_client(subscription_id):

    return StorageManagementClient(
        credential,
        subscription_id
    )


# ======================================================
# Logic App Client
# ======================================================

def get_logic_client(subscription_id):

    return LogicManagementClient(
        credential,
        subscription_id
    )