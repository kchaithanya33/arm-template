from fastapi import APIRouter

from app.services.history_service import (
    get_history
)


router = APIRouter(
    prefix="/history",
    tags=["History"]
)



@router.get("/")
def history():

    return {
        "status":"success",
        "data":get_history()
    }