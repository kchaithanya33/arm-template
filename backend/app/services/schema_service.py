from fastapi import HTTPException



# ======================================================
# Resource Group Validation
# ======================================================

def validate_resource_group(request):


    rg = request.resourceGroup


    # Check mode

    if rg.mode not in [
        "new",
        "existing"
    ]:

        raise HTTPException(

            status_code=400,

            detail="Resource Group mode must be new or existing"

        )


    # Check name

    if not rg.name:

        raise HTTPException(

            status_code=400,

            detail="Resource Group name is required"

        )


    # New Resource Group requires location

    if rg.mode == "new":

        if not rg.location:

            raise HTTPException(

                status_code=400,

                detail="Resource Group location is required for new Resource Group"

            )


    return True
# ======================================================
# Storage Account Validation
# ======================================================

# ======================================================
# Storage Account Validation
# ======================================================

def validate_storage_account(request):


    storage = request.storage



    # Check mode

    if storage.mode not in [

        "new",

        "existing"

    ]:


        raise HTTPException(

            status_code=400,

            detail="Storage Account mode must be new or existing"

        )



    # Check storage name

    if not storage.name:


        raise HTTPException(

            status_code=400,

            detail="Storage Account name is required"

        )



    # ==================================================
    # NEW STORAGE ACCOUNT VALIDATION
    # ==================================================

    if storage.mode == "new":



        # Storage location required

        if not storage.location:


            raise HTTPException(

                status_code=400,

                detail="Storage Account location is required for new Storage Account"

            )



        # SKU required

        if not storage.sku:


            raise HTTPException(

                status_code=400,

                detail="Storage Account SKU is required"

            )



        # Kind required

        if not storage.kind:


            raise HTTPException(

                status_code=400,

                detail="Storage Account Kind is required"

            )



        # ==================================================
        # STORAGE RESOURCE GROUP VALIDATION
        # ==================================================

        if not storage.resourceGroup:


            raise HTTPException(

                status_code=400,

                detail="Storage Resource Group is required for new Storage Account"

            )



        storage_rg = storage.resourceGroup



        if storage_rg.mode not in [

            "new",

            "existing"

        ]:


            raise HTTPException(

                status_code=400,

                detail="Storage Resource Group mode must be new or existing"

            )



        if not storage_rg.name:


            raise HTTPException(

                status_code=400,

                detail="Storage Resource Group name is required"

            )



        # New Storage RG requires location

        if storage_rg.mode == "new":


            if not storage_rg.location:


                raise HTTPException(

                    status_code=400,

                    detail="Storage Resource Group location is required for new Resource Group"

                )





    # ==================================================
    # EXISTING STORAGE ACCOUNT VALIDATION
    # ==================================================

    elif storage.mode == "existing":



        if not storage.resourceId:


            raise HTTPException(

                status_code=400,

                detail="Storage Account resourceId is required for existing Storage Account"

            )



    return True