from fastapi import HTTPException

from arm.arm_deploy import (
    create_resource_group_template,
    create_resource_group_deployment
)

from app.services.rg_parameter_generator import (
    generate_rg_parameters_file
)

from app.services.parameter_generator import (
    generate_parameters_file
)

from app.services.azure_resource_service import (
    validate_resource_group_access,
    validate_storage_account_access
)


# ======================================================
# MAIN DEPLOYMENT FUNCTION
# ======================================================

# ======================================================
# MAIN DEPLOYMENT FUNCTION
# ======================================================

def deploy_application(deployment_request):

    # ------------------------------------------
    # Validate/Create Deployment Resource Group
    # ------------------------------------------

    resource_group_result = process_resource_group(
        deployment_request
    )


    # ------------------------------------------
    # Validate Storage
    # ------------------------------------------

    storage_result = process_storage_account(
        deployment_request
    )


    # ------------------------------------------
    # Validate Logic App
    # ------------------------------------------

    logic_result = process_logic_app(
        deployment_request
    )


    # ------------------------------------------
    # Deploy Storage ARM Template
    # Storage will use its own Resource Group
    # ------------------------------------------

    storage_deployment_result = None


    if deployment_request.storage.mode == "new":


        storage_parameter_file = generate_parameters_file(
            deployment_request
        )


        storage_deployment_result = create_resource_group_deployment(

            resource_group_name=
                deployment_request.storage.resourceGroup.name,

            parameter_file=storage_parameter_file

        )


    # ------------------------------------------
    # Deploy Logic App ARM Template
    # Logic App will use its own Resource Group
    # ------------------------------------------

    logic_parameter_file = generate_parameters_file(
        deployment_request
    )


    logic_deployment_result = create_resource_group_deployment(

        resource_group_name=
            deployment_request.logicApp.resourceGroup.name,

        parameter_file=logic_parameter_file

    )


    return {

        "resourceGroup": resource_group_result,

        "storageAccount": storage_result,

        "logicApp": logic_result,

        "storageDeployment": storage_deployment_result,

        "logicDeployment": logic_deployment_result

    }
# ======================================================
# RESOURCE GROUP
# ======================================================

def process_resource_group(deployment_request):

    subscription_id = deployment_request.subscriptionId

    rg = deployment_request.resourceGroup

    if rg.mode == "new":

        rg_parameter_file = generate_rg_parameters_file(rg)

        create_resource_group_template(
            location=rg.location,
            parameter_file=rg_parameter_file
        )

        return {

            "name": rg.name,

            "mode": "new",

            "status": "created"

        }

    elif rg.mode == "existing":

        access = validate_resource_group_access(
            subscription_id,
            rg.name
        )

        if not access["allowed"]:

            raise HTTPException(
                status_code=403,
                detail=access
            )

        return {

            "name": rg.name,

            "mode": "existing",

            "status": "verified"

        }

    raise HTTPException(
        status_code=400,
        detail="Invalid Resource Group mode"
    )


# ======================================================
# STORAGE ACCOUNT
# ======================================================

def process_storage_account(deployment_request):

    subscription_id = deployment_request.subscriptionId

    storage = deployment_request.storage

    if storage.mode == "new":

        storage_rg = storage.resourceGroup

        if storage_rg.mode == "new":

            rg_parameter_file = generate_rg_parameters_file(
                storage_rg
            )

            create_resource_group_template(
                location=storage_rg.location,
                parameter_file=rg_parameter_file
            )

        elif storage_rg.mode == "existing":

            access = validate_resource_group_access(
                subscription_id,
                storage_rg.name
            )

            if not access["allowed"]:

                raise HTTPException(
                    status_code=403,
                    detail=access
                )

        else:

            raise HTTPException(
                status_code=400,
                detail="Storage Resource Group mode must be new or existing"
            )

        return {

            "name": storage.name,

            "mode": "new",

            "resourceGroup": storage_rg.name,

            "status": "validated"

        }

    elif storage.mode == "existing":

        access = validate_storage_account_access(

            subscription_id,

            storage.resourceId

        )

        if not access["allowed"]:

            raise HTTPException(
                status_code=403,
                detail=access
            )

        return {

            "name": storage.name,

            "mode": "existing",

            "status": "validated"

        }

    raise HTTPException(
        status_code=400,
        detail="Invalid Storage mode"
    )


# ======================================================
# LOGIC APP
# ======================================================

def process_logic_app(deployment_request):

    subscription_id = deployment_request.subscriptionId

    logic = deployment_request.logicApp

    logic_rg = logic.resourceGroup

    if logic_rg.mode == "new":

        rg_parameter_file = generate_rg_parameters_file(
            logic_rg
        )

        create_resource_group_template(
            location=logic_rg.location,
            parameter_file=rg_parameter_file
        )

    elif logic_rg.mode == "existing":

        access = validate_resource_group_access(
            subscription_id,
            logic_rg.name
        )

        if not access["allowed"]:

            raise HTTPException(
                status_code=403,
                detail=access
            )

    else:

        raise HTTPException(
            status_code=400,
            detail="Logic App Resource Group mode must be new or existing"
        )

    return {

        "name": logic.name,

        "mode": "new",

        "resourceGroup": logic_rg.name,

        "status": "validated"

    }