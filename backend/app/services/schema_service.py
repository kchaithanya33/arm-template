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


# ======================================================
# Logic App Validation
# ======================================================

def validate_logic_app(request):

    logic_app = request.logicApp


    # Logic App name

    if not logic_app.name:

        raise HTTPException(

            status_code=400,

            detail="Logic App name is required"

        )


    # Logic App location

    if not logic_app.location:

        raise HTTPException(

            status_code=400,

            detail="Logic App location is required"

        )


    # Resource Group

    if not logic_app.resourceGroup:

        raise HTTPException(

            status_code=400,

            detail="Logic App Resource Group is required"

        )


    logic_rg = logic_app.resourceGroup


    # Mode

    if logic_rg.mode not in [

        "new",

        "existing"

    ]:

        raise HTTPException(

            status_code=400,

            detail="Logic App Resource Group mode must be new or existing"

        )


    # Name

    if not logic_rg.name:

        raise HTTPException(

            status_code=400,

            detail="Logic App Resource Group name is required"

        )


    # New Resource Group requires location

    if logic_rg.mode == "new":

        if not logic_rg.location:

            raise HTTPException(

                status_code=400,

                detail="Logic App Resource Group location is required"

            )


    return True


# ======================================================
# Function App Validation
# ======================================================

def validate_function_app(request):

    function_app = request.functionApp


    # ==================================================
    # FUNCTION APP BASIC VALIDATION
    # ==================================================

    if not function_app.name:

        raise HTTPException(
            status_code=400,
            detail="Function App name is required"
        )


    if not function_app.location:

        raise HTTPException(
            status_code=400,
            detail="Function App location is required"
        )


    if not function_app.runtimeStack:

        raise HTTPException(
            status_code=400,
            detail="Function App runtime stack is required"
        )


    if not function_app.runtimeVersion:

        raise HTTPException(
            status_code=400,
            detail="Function App runtime version is required"
        )


    # ==================================================
    # FUNCTION APP STORAGE VALIDATION
    # ==================================================

    if not function_app.storageAccount:

        raise HTTPException(
            status_code=400,
            detail="Function App Storage Account is required"
        )


    storage = function_app.storageAccount


    if storage.mode not in [
        "new",
        "existing"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Function App Storage mode must be new or existing"
        )


    if not storage.name:

        raise HTTPException(
            status_code=400,
            detail="Function App Storage Account name is required"
        )


    # Existing Storage Account

    if storage.mode == "existing":

        if not storage.resourceId:

            raise HTTPException(
                status_code=400,
                detail="Storage Account resourceId is required for existing Storage Account"
            )


    # New Storage Account

    if storage.mode == "new":

        if not storage.location:

            raise HTTPException(
                status_code=400,
                detail="Storage Account location is required for new Storage Account"
            )


    # ==================================================
    # FUNCTION APP RESOURCE GROUP VALIDATION
    # ==================================================

    if not function_app.resourceGroup:

        raise HTTPException(
            status_code=400,
            detail="Function App Resource Group is required"
        )


    function_rg = function_app.resourceGroup


    if function_rg.mode not in [
        "new",
        "existing"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Function App Resource Group mode must be new or existing"
        )


    if not function_rg.name:

        raise HTTPException(
            status_code=400,
            detail="Function App Resource Group name is required"
        )


    # New Resource Group requires location

    if function_rg.mode == "new":

        if not function_rg.location:

            raise HTTPException(
                status_code=400,
                detail="Function App Resource Group location is required"
            )


    return True