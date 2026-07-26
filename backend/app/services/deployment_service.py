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
    validate_storage_account_access,
    validate_storage_resource_group
)



# ======================================================
# MAIN DEPLOYMENT FUNCTION
# ======================================================

def deploy_application(
        deployment_request
):


    # 1. Resource Group

    resource_group_result = process_resource_group(
        deployment_request
    )


    # 2. Storage Account

    storage_result = process_storage_account(
        deployment_request
    )


    return {


        "resourceGroup": resource_group_result,


        "storageAccount": storage_result


    }



# ======================================================
# RESOURCE GROUP DEPLOYMENT FLOW
# ======================================================

def process_resource_group(
        deployment_request
):


    subscription_id = deployment_request.subscriptionId


    deployment_rg = deployment_request.resourceGroup



    # ==================================================
    # CREATE NEW RESOURCE GROUP
    # ==================================================

    if deployment_rg.mode == "new":



        rg_parameter_file = generate_rg_parameters_file(

            deployment_rg

        )



        rg_result = create_resource_group_template(

            location=deployment_rg.location,

            parameter_file=rg_parameter_file

        )



        return {


            "name": deployment_rg.name,

            "mode": "new",

            "status": "created",

            "deployment": rg_result

        }




    # ==================================================
    # EXISTING RESOURCE GROUP
    # ==================================================

    elif deployment_rg.mode == "existing":



        rg_access = validate_resource_group_access(

            subscription_id,

            deployment_rg.name

        )



        if not rg_access["allowed"]:


            raise HTTPException(

                status_code=403,

                detail=rg_access

            )



        return {


            "name": deployment_rg.name,

            "mode": "existing",

            "status": "access_verified"

        }
# ======================================================
# STORAGE ACCOUNT DEPLOYMENT FLOW
# ======================================================


# ======================================================
# STORAGE ACCOUNT DEPLOYMENT FLOW
# ======================================================

def process_storage_account(
        deployment_request
):


    subscription_id = deployment_request.subscriptionId

    storage = deployment_request.storage


    storage_resource_group = storage.resourceGroup



    # ======================================================
    # NEW STORAGE ACCOUNT
    # ======================================================

    if storage.mode == "new":



        # ==================================================
        # STORAGE RESOURCE GROUP HANDLING
        # ==================================================

        if storage_resource_group.mode == "new":



            # Generate RG parameters

            rg_parameter_file = generate_rg_parameters_file(

                storage_resource_group

            )


            # Create Storage Resource Group
            # Subscription Scope Deployment

            create_resource_group_template(

                location=storage_resource_group.location,

                parameter_file=rg_parameter_file

            )



        elif storage_resource_group.mode == "existing":



            # Validate existing Storage Resource Group

            rg_access = validate_resource_group_access(

                subscription_id,

                storage_resource_group.name

            )


            if not rg_access["allowed"]:

                raise HTTPException(

                    status_code=403,

                    detail=rg_access

                )



        else:

            raise HTTPException(

                status_code=400,

                detail="Storage Resource Group mode must be new or existing"

            )



        # ==================================================
        # Generate Storage ARM Parameters
        # ==================================================

        parameter_file = generate_parameters_file(

            deployment_request

        )



        # ==================================================
        # Deploy Storage Account
        # Resource Group Scope
        # ==================================================

        storage_result = create_resource_group_deployment(

            resource_group_name=storage_resource_group.name,

            parameter_file=parameter_file

        )



        return {


            "name": storage.name,

            "mode": "new",

            "resourceGroup": storage_resource_group.name,

            "status": "created",

            "deployment": storage_result

        }





    # ======================================================
    # EXISTING STORAGE ACCOUNT
    # ======================================================

    elif storage.mode == "existing":



        storage_access = validate_storage_account_access(

            subscription_id,

            storage.resourceId

        )


        if not storage_access["allowed"]:


            raise HTTPException(

                status_code=403,

                detail=storage_access

            )



        return {


            "name": storage.name,

            "mode": "existing",

            "resourceId": storage.resourceId,

            "status": "access_verified"

        }




    else:


        raise HTTPException(

            status_code=400,

            detail="Storage mode must be new or existing"

        )