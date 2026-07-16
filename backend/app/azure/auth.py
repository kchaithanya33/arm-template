
from azure.identity import DefaultAzureCredential

# Uses your Azure CLI login (az login)
credential = DefaultAzureCredential()

# Replace with your Azure Subscription ID
SUBSCRIPTION_ID = "cc65e704-15de-4ddc-aa64-56973ac617f8"


def get_credential():
    """
    Returns the Azure credential.
    """
    return credential


def get_subscription_id():
    """
    Returns the Azure Subscription ID.
    """
    return SUBSCRIPTION_ID

