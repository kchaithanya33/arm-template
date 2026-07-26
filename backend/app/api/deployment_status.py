from fastapi import APIRouter, HTTPException

from services.deployment_status import (
    get_deployment_status
)


router = APIRouter(
    prefix="/deployment",
    tags=["Deployment Status"]
)



@router.get("/{deployment_name}")
def status(deployment_name:str):

    try:

        return get_deployment_status(
            deployment_name
        )


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )