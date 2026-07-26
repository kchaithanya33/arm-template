from fastapi import APIRouter, HTTPException

from app.models.deployment_model import (
    DeploymentRequest
)

from app.services.deployment_service import (
    deploy_application
)



router = APIRouter(

    prefix="/deployment",

    tags=["Deployment"]

)



# ======================================================
# Start Deployment API
# ======================================================

@router.post("/")
def create_deployment(

        deployment_request: DeploymentRequest

):

    try:

        print("\n==============================")
        print("DEPLOYMENT REQUEST RECEIVED")
        print("==============================\n")


        print(
            deployment_request.model_dump_json(
                indent=4
            )
        )


        result = deploy_application(

            deployment_request

        )


        return {

            "status": "success",

            "message":
            "Deployment request completed",

            "data":
            result

        }



    except HTTPException as e:

        raise e



    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )