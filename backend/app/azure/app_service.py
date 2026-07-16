from azure.mgmt.web import WebSiteManagementClient

from app.azure.auth import get_credential, get_subscription_id


# Create WebSite Management client
client = WebSiteManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


def get_app_service_plans():
    """
    Returns all App Service Plans in the current subscription.
    """

    app_service_plans = []

    for plan in client.app_service_plans.list():

        app_service_plans.append(
            {
                "id": plan.id,
                "name": plan.name,
                "location": plan.location,
                "resource_group": plan.id.split("/")[4],
                "sku": plan.sku.name if plan.sku else None,
                "tier": plan.sku.tier if plan.sku else None,
                "kind": plan.kind
            }
        )

    return app_service_plans


