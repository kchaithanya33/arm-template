from pydantic import BaseModel


# ======================================================
# Resource Group Model
# ======================================================

class ResourceGroupModel(BaseModel):

    # new or existing
    mode: str

    # Resource Group Name
    name: str

    # Required only for new Resource Group
    location: str | None = None



# ======================================================
# Main Deployment Request
# ======================================================

class DeploymentRequest(BaseModel):

    # Azure Subscription ID
    subscriptionId: str

    # Deployment Resource Group
    resourceGroup: ResourceGroupModel