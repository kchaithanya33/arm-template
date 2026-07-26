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
# Storage Resource Group Model
# ======================================================

class StorageResourceGroupModel(BaseModel):

    # new or existing
    mode: str

    # Resource Group Name
    name: str

    # Required only for new
    location: str | None = None

# ======================================================
# Storage Account Model
# ======================================================

# ======================================================
# Storage Account Model
# ======================================================

class StorageAccountModel(BaseModel):

    # new or existing
    mode: str

    # Storage Account Name
    name: str


    # Resource Group for this Storage Account

    resourceGroup: StorageResourceGroupModel| None = None



    # NEW STORAGE ONLY

    location: str | None = None

    kind: str | None = "StorageV2"

    sku: str | None = "Standard_LRS"

    accessTier: str | None = "Hot"

    publicNetworkAccess: str | None = "Enabled"

    minimumTlsVersion: str | None = "TLS1_2"

    secureTransferRequired: bool | None = True

    allowBlobPublicAccess: bool | None = False

    allowSharedKeyAccess: bool | None = True

    largeFileSharesState: str | None = "Disabled"


    # EXISTING STORAGE ONLY

    resourceId: str | None = None



# ======================================================
# Logic App Resource Group Model
# ======================================================

class LogicAppResourceGroupModel(BaseModel):

    # new or existing
    mode: str

    # Resource Group Name
    name: str

    # Required only for new
    location: str | None = None

# ======================================================
# Logic App Model
# ======================================================

class LogicAppModel(BaseModel):

    # Always new (for now)
    mode: str

    # Logic App Name
    name: str

    # Logic App Location
    location: str

    # Resource Group
    resourceGroup: LogicAppResourceGroupModel


# ======================================================
# Main Deployment Request
# ======================================================

class DeploymentRequest(BaseModel):


    # Azure Subscription ID
    subscriptionId: str


    # Deployment Resource Group
    resourceGroup: ResourceGroupModel



    # Storage Account
    storage: StorageAccountModel
    
    logicApp: LogicAppModel