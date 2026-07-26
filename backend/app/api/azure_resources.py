from fastapi import APIRouter, HTTPException

from app.services.azure_resource_service import (
    get_resource_groups,
    get_locations
)


router = APIRouter(
    prefix="/azure",
    tags=["Azure Resources"]
)


# ======================================================
# RESOURCE GROUPS
# ======================================================

@router.get("/resource-groups")
def resource_groups(subscription_id: str):

    try:

        return {
            "status": "success",
            "data": get_resource_groups(subscription_id)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ======================================================
# LOCATIONS
# ======================================================

@router.get("/locations")
def locations(subscription_id: str):

    try:

        return {
            "status": "success",
            "data": get_locations(subscription_id)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )