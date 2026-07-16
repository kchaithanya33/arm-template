from fastapi import APIRouter

from app.azure.resource_group import get_resource_groups
from app.azure.location import get_locations
from app.azure.storage import get_storage_accounts
from app.azure.app_service import get_app_service_plans
from app.azure.function_app import get_function_apps
from app.azure.logic_app import get_logic_apps

router = APIRouter(prefix="/azure", tags=["Azure"])


@router.get("/resource-groups")
def resource_groups():
    return get_resource_groups()


@router.get("/locations")
def locations():
    return get_locations()


@router.get("/storage-accounts")
def storage_accounts():
    return get_storage_accounts()


@router.get("/app-service-plans")
def app_service_plans():
    return get_app_service_plans()


@router.get("/function-apps")
def function_apps():
    return get_function_apps()


@router.get("/logic-apps")
def logic_apps():
    return get_logic_apps()

from app.azure.application_insights import get_application_insights


@router.get("/application-insights")
def application_insights():
    return get_application_insights()