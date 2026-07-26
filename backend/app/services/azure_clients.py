from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.applicationinsights import ApplicationInsightsManagementClient
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.web import WebSiteManagementClient



# ======================================================
# Authentication
# ======================================================

def get_credential():

    return DefaultAzureCredential()



# ======================================================
# Resource Client
# ======================================================

def get_resource_client(subscription_id):

    return ResourceManagementClient(
        get_credential(),
        subscription_id
    )



# ======================================================
# Storage Client
# ======================================================

def get_storage_client(subscription_id):

    return StorageManagementClient(
        get_credential(),
        subscription_id
    )



# ======================================================
# Application Insights Client
# ======================================================

def get_appinsights_client(subscription_id):

    return ApplicationInsightsManagementClient(
        get_credential(),
        subscription_id
    )



# ======================================================
# Log Analytics Client
# ======================================================

def get_loganalytics_client(subscription_id):

    return LogAnalyticsManagementClient(
        get_credential(),
        subscription_id
    )



# ======================================================
# Web Client
# Used for App Service / Function Apps
# ======================================================

def get_web_client(subscription_id):

    return WebSiteManagementClient(
        get_credential(),
        subscription_id
    )



# ======================================================
# Subscription Client
# ======================================================

def get_subscription_client():

    return SubscriptionClient(
        get_credential()
    )