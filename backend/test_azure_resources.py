from app.services.azure_resource_service import *


SUBSCRIPTION_ID="cc65e704-15de-4ddc-aa64-56973ac617f8"


print(get_resource_groups(SUBSCRIPTION_ID))

print(get_storage_accounts(SUBSCRIPTION_ID))

print(get_application_insights(SUBSCRIPTION_ID))

print(get_locations(SUBSCRIPTION_ID))

print(get_function_runtimes())

print(get_storage_options())