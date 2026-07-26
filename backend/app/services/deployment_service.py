from fastapi import HTTPException

from app.services.rg_parameter_generator import (
    generate_rg_parameters_file
)

from app.services.azure_resource_service import (
    validate_resource_group_access
)

from arm.arm_deploy import (
    create_resource_group_template
)



# ======================================================
# MAIN DEPLOYMENT FUNCTION
# ======================================================

def deploy_application(
        deployment_request
):


    # Resource Group deployment

    resource_group_result = process_resource_group(
        deployment_request
    )


    return {

        "resourceGroup": resource_group_result

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