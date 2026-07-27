import json
from pathlib import Path



# ======================================================
# Generate ARM Parameters File
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



        "storageMode": {

            "value":
            storage.mode

        },


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


            "storageResourceGroupName": {

                "value":
                storage.resourceGroup.name

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
    # FUNCTION APP PARAMETERS  (NEW)
    # ==================================================

    function_app = getattr(
        deployment_request,
        "functionApp",
        None
    )



    if function_app:



        function_parameters = {


            "functionAppName": {

                "value":
                function_app.name

            },


            "functionAppLocation": {

                "value":
                function_app.location

            },


            "functionRuntimeStack": {

                "value":
                function_app.runtimeStack

            },


            "functionRuntimeVersion": {

                "value":
                function_app.runtimeVersion

            },


            "functionResourceGroupName": {

                "value":
                function_app.resourceGroup.name

            }

        }




        # ==================================================
        # FUNCTION APP STORAGE
        # ==================================================

        function_storage = function_app.storageAccount



        function_parameters.update({


            "functionStorageMode": {

                "value":
                function_storage.mode

            },


            "functionStorageAccountName": {

                "value":
                function_storage.name

            }

        })




        # ==================================================
        # NEW FUNCTION STORAGE DEFAULT VALUES
        # ==================================================

        if function_storage.mode == "new":


            function_parameters.update({


                "functionStorageLocation": {

                    "value":
                    function_storage.location

                },


                "functionStorageKind": {

                    "value":
                    function_storage.kind
                    if function_storage.kind
                    else "StorageV2"

                },


                "functionStorageSku": {

                    "value":
                    function_storage.sku
                    if function_storage.sku
                    else "Standard_LRS"

                },


                "functionStorageAccessTier": {

                    "value":
                    function_storage.accessTier
                    if function_storage.accessTier
                    else "Hot"

                },


                "functionStoragePublicNetworkAccess": {

                    "value":
                    function_storage.publicNetworkAccess
                    if function_storage.publicNetworkAccess
                    else "Enabled"

                },


                "functionStorageMinimumTlsVersion": {

                    "value":
                    function_storage.minimumTlsVersion
                    if function_storage.minimumTlsVersion
                    else "TLS1_2"

                },


                "functionStorageSecureTransferRequired": {

                    "value":
                    function_storage.secureTransferRequired
                    if function_storage.secureTransferRequired is not None
                    else True

                },


                "functionStorageAllowBlobPublicAccess": {

                    "value":
                    function_storage.allowBlobPublicAccess
                    if function_storage.allowBlobPublicAccess is not None
                    else False

                },


                "functionStorageAllowSharedKeyAccess": {

                    "value":
                    function_storage.allowSharedKeyAccess
                    if function_storage.allowSharedKeyAccess is not None
                    else True

                },


                "functionStorageLargeFileSharesState": {

                    "value":
                    function_storage.largeFileSharesState
                    if function_storage.largeFileSharesState
                    else "Disabled"

                }

            })



        parameters["parameters"].update(
            function_parameters
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