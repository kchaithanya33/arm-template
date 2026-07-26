import json
from pathlib import Path



# ======================================================
# Generate Storage Account ARM Parameters
# ======================================================

def generate_parameters_file(deployment_request):


    storage = deployment_request.storage



    parameters = {


        "$schema":
        "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",


        "contentVersion":
        "1.0.0.0",


        "parameters": {}

    }



    # ==================================================
    # STORAGE ACCOUNT
    # ==================================================

    if not storage:

        raise ValueError(
            "Storage Account details required"
        )



    storage_parameters = {



        # New / Existing

        "storageMode": {

            "value":
            storage.mode

        },



        # Storage Account Name

        "storageAccountName": {

            "value":
            storage.name

        }

    }




    # ==================================================
    # NEW STORAGE ACCOUNT
    # ==================================================

    if storage.mode == "new":



        storage_parameters.update({



            "storageLocation": {

                "value":
                storage.location

            },



            "storageKind": {

                "value":
                storage.kind

            },



            "storageSku": {

                "value":
                storage.sku

            },



            "accessTier": {

                "value":
                storage.accessTier
                if storage.accessTier
                else "Hot"

            },



            "publicNetworkAccess": {

                "value":
                storage.publicNetworkAccess
                if storage.publicNetworkAccess
                else "Enabled"

            },



            "minimumTlsVersion": {

                "value":
                storage.minimumTlsVersion
                if storage.minimumTlsVersion
                else "TLS1_2"

            },



            "secureTransferRequired": {

                "value":
                storage.secureTransferRequired
                if storage.secureTransferRequired is not None
                else True

            },



            "allowBlobPublicAccess": {

                "value":
                storage.allowBlobPublicAccess
                if storage.allowBlobPublicAccess is not None
                else False

            },



            "allowSharedKeyAccess": {

                "value":
                storage.allowSharedKeyAccess
                if storage.allowSharedKeyAccess is not None
                else True

            },



            "largeFileSharesState": {

                "value":
                storage.largeFileSharesState
                if storage.largeFileSharesState
                else "Disabled"

            }

        })



        parameters["parameters"].update(
            storage_parameters
        )



    # ==================================================
    # EXISTING STORAGE ACCOUNT
    # ==================================================

    elif storage.mode == "existing":


        parameters["parameters"].update(
            {

                "storageMode": {

                    "value":
                    "existing"

                },

                "storageAccountName": {

                    "value":
                    storage.name

                }

            }
        )



    else:


        raise ValueError(
            "Storage mode must be new or existing"
        )



    # ==================================================
    # LOGIC APP PARAMETERS
    # ==================================================

    logic_app = getattr(
        deployment_request,
        "logicApp",
        None
    )


    if logic_app:


        logic_parameters = {


            "logicAppName": {

                "value":
                logic_app.name

            },


            "logicAppLocation": {

                "value":
                logic_app.location

            },


            "logicAppMode": {

                "value":
                logic_app.mode

            }

        }



        # Logic App Resource Group

        if logic_app.resourceGroup:


            logic_parameters.update({

                "logicAppResourceGroupName": {

                    "value":
                    logic_app.resourceGroup.name

                }

            })



        parameters["parameters"].update(
            logic_parameters
        )



    # ==================================================
    # WRITE PARAMETERS FILE
    # ==================================================

    output_folder = Path(
        "arm/generated"
    )


    output_folder.mkdir(
        exist_ok=True
    )



    file_path = (

        output_folder /

        "parameters.json"

    )



    with open(
        file_path,
        "w"
    ) as file:


        json.dump(

            parameters,

            file,

            indent=4

        )



    return file_path