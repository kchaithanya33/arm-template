from azure.mgmt.applicationinsights import ApplicationInsightsManagementClient

from app.azure.auth import get_credential, get_subscription_id


client = ApplicationInsightsManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


def get_application_insights():

    result = []

    for app in client.components.list():

        result.append(
            {
                "id": app.id,
                "name": app.name,
                "location": app.location,
                "resource_group": app.id.split("/")[4]
            }
        )

    return result


if __name__ == "__main__":

    from pprint import pprint

    pprint(get_application_insights())