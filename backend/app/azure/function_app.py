from azure.mgmt.web import WebSiteManagementClient

from app.azure.auth import get_credential, get_subscription_id


# Create WebSite Management client
client = WebSiteManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


def get_function_apps():
    """
    Returns all Function Apps in the current subscription.
    """

    function_apps = []

    for app in client.web_apps.list():

        if app.kind and "functionapp" in app.kind:

            function_apps.append(
                {
                    "id": app.id,
                    "name": app.name,
                    "location": app.location,
                    "resource_group": app.id.split("/")[4],
                    "state": app.state,
                    "kind": app.kind
                }
            )

    return function_apps


# --------------------------------
# Temporary Test
# --------------------------------
if __name__ == "__main__":

    from pprint import pprint

    pprint(get_function_apps())