from azure.mgmt.subscription import SubscriptionClient

from app.azure.auth import get_credential, get_subscription_id


# Create Subscription client
client = SubscriptionClient(
    credential=get_credential()
)


def get_locations():
    """
    Returns all Azure locations available for the current subscription.
    """

    locations = client.subscriptions.list_locations(
        get_subscription_id()
    )

    result = []

    for location in locations:

        result.append(
            {
                "name": location.name,
                "display_name": location.display_name
            }
        )

    return result


