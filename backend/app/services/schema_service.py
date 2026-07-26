from fastapi import HTTPException


# ======================================================
# Resource Group Validation
# ======================================================

def validate_resource_group(request):

    rg = request.resourceGroup


    # --------------------------------------------------
    # Check mode
    # --------------------------------------------------

    if rg.mode not in ["new", "existing"]:

        raise HTTPException(
            status_code=400,
            detail="Resource Group mode must be new or existing"
        )


    # --------------------------------------------------
    # Check Resource Group Name
    # --------------------------------------------------

    if not rg.name:

        raise HTTPException(
            status_code=400,
            detail="Resource Group name is required"
        )


    # --------------------------------------------------
    # New Resource Group
    # Location required
    # --------------------------------------------------

    if rg.mode == "new":

        if not rg.location:

            raise HTTPException(
                status_code=400,
                detail="Resource Group location is required for new resource group"
            )


    return True