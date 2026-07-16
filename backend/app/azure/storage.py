from azure.mgmt.storage import StorageManagementClient

from app.azure.auth import get_credential, get_subscription_id


# Create Storage Management client
client = StorageManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


def get_storage_accounts():
    """
    Returns all Storage Accounts in the current subscription.
    """

    storage_accounts = []

    for account in client.storage_accounts.list():

        storage_accounts.append(
            {
                "id": account.id,
                "name": account.name,
                "location": account.location,
                "sku": account.sku.name,
                "resource_group": account.id.split("/")[4]
            }
        )

    return storage_accounts


