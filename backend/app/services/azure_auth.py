from azure.identity import DefaultAzureCredential


# Create credential once
credential = DefaultAzureCredential()


def get_credential():
    return credential