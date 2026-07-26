# import json
# from pathlib import Path


# # ======================================================
# # Generate ARM Parameters
# # ======================================================

# def generate_parameters_file(deployment_request):


#     storage = deployment_request.storage

#     logic_app = deployment_request.logicApp


#     parameters = {

#         "$schema":
#         "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",


#         "contentVersion":
#         "1.0.0.0",


#         "parameters": {}

#     }



#     # ==================================================
#     # STORAGE ACCOUNT
#     # ==================================================

#     if storage:


#         storage_parameters = {


#             "storageMode": {

#                 "value":
#                 storage.mode

#             },


#             "storageAccountName": {

#                 "value":
#                 storage.name

#             }

#         }



#         # ------------------------------
#         # NEW STORAGE
#         # ------------------------------

#         if storage.mode == "new":


#             storage_parameters.update({


#                 "storageLocation": {

#                     "value":
#                     storage.location

#                 },


#                 "storageKind": {

#                     "value":
#                     storage.kind

#                 },


#                 "storageSku": {

#                     "value":
#                     storage.sku

#                 },


#                 "accessTier": {

#                     "value":
#                     storage.accessTier

#                 },


#                 "publicNetworkAccess": {

#                     "value":
#                     storage.publicNetworkAccess

#                 },


#                 "minimumTlsVersion": {

#                     "value":
#                     storage.minimumTlsVersion

#                 },


#                 "secureTransferRequired": {

#                     "value":
#                     storage.secureTransferRequired

#                 },


#                 "encryptionType": {

#                     "value":
#                     storage.encryptionType

#                 },


#                 "allowBlobPublicAccess": {

#                     "value":
#                     storage.allowBlobPublicAccess

#                 },


#                 "allowSharedKeyAccess": {

#                     "value":
#                     storage.allowSharedKeyAccess

#                 },


#                 "largeFileSharesState": {

#                     "value":
#                     storage.largeFileSharesState
#                     if storage.largeFileSharesState
#                     else "Disabled"

#                 }

#             })



#         # ------------------------------
#         # EXISTING STORAGE
#         # ------------------------------

#         elif storage.mode == "existing":


#             storage_parameters.update({


#                 "existingStorageResourceId": {

#                     "value":
#                     storage.existingResourceId
#                     if storage.existingResourceId
#                     else ""

#                 },


#                 "existingStorageConnectionString": {

#                     "value":
#                     storage.existingConnectionString
#                     if storage.existingConnectionString
#                     else ""

#                 }

#             })



#         parameters["parameters"].update(
#             storage_parameters
#         )





#     # ==================================================
#     # LOGIC APP
#     # ==================================================

#     if logic_app:


#         parameters["parameters"].update({


#             "logicAppMode": {

#                 "value":
#                 "new"

#             },


#             "logicAppName": {

#                 "value":
#                 logic_app.name

#             },


#             "logicAppLocation": {

#                 "value":
#                 logic_app.location

#             },


#             "workflowType": {

#                 "value":
#                 logic_app.workflowType

#             }

#         })





#         # ==================================================
#         # APPLICATION INSIGHTS
#         # ==================================================

#         app_insights = logic_app.applicationInsights



#         if app_insights:


#             app_parameters = {


#                 "applicationInsightsMode": {

#                     "value":
#                     app_insights.mode

#                 },


#                 "applicationInsightsName": {

#                     "value":
#                     app_insights.name

#                 }

#             }



#             # NEW APP INSIGHTS

#             if app_insights.mode == "new":


#                 app_parameters.update({


#                     "applicationInsightsLocation": {

#                         "value":
#                         app_insights.location

#                     },


#                     "applicationType": {

#                         "value":
#                         app_insights.applicationType

#                     },


#                     "applicationInsightsRetentionInDays": {

#                         "value":
#                         app_insights.retentionInDays
#                         if app_insights.retentionInDays
#                         else 90

#                     }

#                 })



#             # EXISTING APP INSIGHTS

#             elif app_insights.mode == "existing":


#                 app_parameters.update({


#                     "existingApplicationInsightsResourceId": {

#                         "value":
#                         app_insights.existingResourceId
#                         if hasattr(app_insights, "existingResourceId")
#                         else ""

#                     }

#                 })



#             parameters["parameters"].update(
#                 app_parameters
#             )






#             # ==================================================
#             # LOG ANALYTICS WORKSPACE
#             # ==================================================

#             workspace = app_insights.workspace



#             if workspace:


#                 workspace_parameters = {


#                     "workspaceMode": {

#                         "value":
#                         workspace.mode

#                     },


#                     "workspaceName": {

#                         "value":
#                         workspace.name

#                     }

#                 }



#                 # NEW WORKSPACE

#                 if workspace.mode == "new":


#                     workspace_parameters.update({


#                         "workspaceLocation": {

#                             "value":
#                             workspace.location

#                         },


#                         "workspaceSku": {

#                             "value":
#                             workspace.sku

#                         }

#                     })



#                 # EXISTING WORKSPACE

#                 elif workspace.mode == "existing":


#                     workspace_parameters.update({


#                         "existingWorkspaceResourceId": {

#                             "value":
#                             workspace.existingResourceId
#                             if workspace.existingResourceId
#                             else ""

#                         }

#                     })



#                 parameters["parameters"].update(
#                     workspace_parameters
#                 )







#     # ==================================================
#     # WRITE PARAMETERS FILE
#     # ==================================================

#     output_folder = Path(
#         "arm/generated"
#     )


#     output_folder.mkdir(
#         exist_ok=True
#     )



#     file_path = (

#         output_folder

#         /

#         "parameters.json"

#     )



#     with open(
#         file_path,
#         "w"
#     ) as file:


#         json.dump(

#             parameters,

#             file,

#             indent=4

#         )


#     return file_path

import json
from pathlib import Path


# ======================================================
# Generate ARM Parameters
# ======================================================

def generate_parameters_file(deployment_request):


    storage = deployment_request.storage
    logic_app = deployment_request.logicApp


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

    if storage:


        storage_parameters = {


            "storageMode": {

                "value": storage.mode

            },


            "storageAccountName": {

                "value": storage.name

            }

        }



        # ------------------------------
        # NEW STORAGE
        # ------------------------------

        if storage.mode == "new":


            storage_parameters.update({


                "storageLocation": {

                    "value": storage.location

                },


                "storageKind": {

                    "value": storage.kind

                },


                "storageSku": {

                    "value": storage.sku

                },


                "accessTier": {

                    "value": storage.accessTier

                },


                "publicNetworkAccess": {

                    "value": storage.publicNetworkAccess

                },


                "minimumTlsVersion": {

                    "value": storage.minimumTlsVersion

                },


                "secureTransferRequired": {

                    "value": storage.secureTransferRequired

                },


                "encryptionType": {

                    "value": storage.encryptionType

                },


                "allowBlobPublicAccess": {

                    "value": storage.allowBlobPublicAccess

                },


                "allowSharedKeyAccess": {

                    "value": storage.allowSharedKeyAccess

                },


                "largeFileSharesState": {

                    "value":
                    storage.largeFileSharesState
                    if storage.largeFileSharesState
                    else "Disabled"

                }

            })



        # ------------------------------
        # EXISTING STORAGE
        # ------------------------------

        elif storage.mode == "existing":


            storage_parameters.update({


                "existingStorageResourceId": {

                    "value":
                    storage.existingResourceId
                    if storage.existingResourceId
                    else ""

                },


                "existingStorageConnectionString": {

                    "value":
                    storage.existingConnectionString
                    if storage.existingConnectionString
                    else ""

                }

            })



        parameters["parameters"].update(
            storage_parameters
        )





    # ==================================================
    # LOGIC APP
    # ==================================================

    if logic_app:


        parameters["parameters"].update({


            "logicAppMode": {

                "value": "new"

            },


            "logicAppName": {

                "value": logic_app.name

            },


            "logicAppLocation": {

                "value": logic_app.location

            },


            "workflowType": {

                "value": logic_app.workflowType

            }

        })




        # ==================================================
        # APPLICATION INSIGHTS
        # ==================================================

        app_insights = logic_app.applicationInsights



        if app_insights:


            app_parameters = {


                "applicationInsightsMode": {

                    "value": app_insights.mode

                },


                "applicationInsightsName": {

                    "value": app_insights.name

                }

            }



            # ------------------------------
            # NEW APPLICATION INSIGHTS
            # ------------------------------

            if app_insights.mode == "new":


                app_parameters.update({


                    "applicationInsightsLocation": {

                        "value": app_insights.location

                    },


                    "applicationType": {

                        "value": app_insights.applicationType

                    },


                    "applicationInsightsRetentionInDays": {

                        "value":
                        app_insights.retentionInDays
                        if app_insights.retentionInDays
                        else 90

                    }

                })



            # ------------------------------
            # EXISTING APPLICATION INSIGHTS
            # Only name required
            # ------------------------------

            elif app_insights.mode == "existing":


                app_parameters.update({


                    "existingApplicationInsightsResourceId": {

                        "value": ""

                    }

                })



            parameters["parameters"].update(
                app_parameters
            )





            # ==================================================
            # LOG ANALYTICS WORKSPACE
            # ==================================================

            workspace = app_insights.workspace



            if workspace:


                workspace_parameters = {


                    "workspaceMode": {

                        "value": workspace.mode

                    },


                    "workspaceName": {

                        "value": workspace.name

                    }

                }




                # ------------------------------
                # NEW WORKSPACE
                # ------------------------------

                if workspace.mode == "new":


                    workspace_parameters.update({


                        "workspaceLocation": {

                            "value": workspace.location

                        },


                        "workspaceSku": {

                            "value": workspace.sku

                        }

                    })




                # ------------------------------
                # EXISTING WORKSPACE
                # Only name required
                # ------------------------------

                elif workspace.mode == "existing":


                    workspace_parameters.update({


                        "existingWorkspaceResourceId": {

                            "value": ""

                        }

                    })



                parameters["parameters"].update(
                    workspace_parameters
                )





    # ==================================================
    # WRITE FILE
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