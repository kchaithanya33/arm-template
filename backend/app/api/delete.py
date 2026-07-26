from fastapi import APIRouter, HTTPException

from app.models.delete_model import DeleteRequest
from app.services.delete_service import delete_resource


router = APIRouter(
    prefix="/delete",
    tags=["Delete"]
)



@router.post("/")
def delete(request: DeleteRequest):

    try:

        result = delete_resource(
            request.subscription_id,
            request.resource_group,
            request.resource_name,
            request.resource_type
        )

        return result


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )