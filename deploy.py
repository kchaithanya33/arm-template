
# import json
# import subprocess
# from pathlib import Path
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import ResourceManagementClient
# from azure.core.exceptions import ResourceNotFoundError


# class AzureDeployment:
#     # ======================================================
#     # Constructor
#     # ======================================================
#     def __init__(self):
#         self.subscription_id = input("Subscription ID: ")
#         self.credential = DefaultAzureCredential()
#         self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)
#         self.template_folder = Path("templates")
#         self.generated_folder = Path("generated")
#         self.generated_folder.mkdir(exist_ok=True)

#     # ======================================================
#     # Execute Azure CLI
#     # ======================================================
#     def execute(self, command):
#         print("\n================================")
#         print("Executing")
#         print("================================\n")
#         print(" ".join(command))
#         result = subprocess.run(command, capture_output=True, text=True, shell=True)
#         print("\nSTDOUT")
#         print(result.stdout)
#         print("\nSTDERR")
#         print(result.stderr)
#         return result

#     # ======================================================
#     # Resource Group
#     # ======================================================
#     def resource_group(self):
#         print("\n==============================")
#         print("RESOURCE GROUP")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Resource Group Name: ")
#             try:
#                 rg = self.resource_client.resource_groups.get(name)
#                 print("\nUsing Existing Resource Group")
#                 return {"name": rg.name, "location": rg.location, "mode": "existing"}
#             except ResourceNotFoundError:
#                 raise Exception("Resource Group not found")
#         else:
#             name = input("New Resource Group Name: ")
#             location = input("Location: ")
#             self.resource_client.resource_groups.create_or_update(name, {"location": location})
#             print("\nResource Group Created")
#             return {"name": name, "location": location, "mode": "new"}

#     # ======================================================
#     # Storage Account
#     # ======================================================
#     def storage_account(self):
#         print("\n==============================")
#         print("STORAGE ACCOUNT")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Storage Account Name: ")
#             return {"mode": "existing", "name": name}
#         name = input("Storage Account Name: ")
#         location = input("Storage Location: ")
#         kind = input("Kind (StorageV2): ") or "StorageV2"
#         sku = input("SKU (Standard_LRS): ") or "Standard_LRS"
#         tier = input("Access Tier (Hot/Cool): ") or "Hot"
#         network = input("Public Network Access (Enabled/Disabled): ") or "Enabled"
#         tls = input("Minimum TLS Version (TLS1_2): ") or "TLS1_2"
#         encryption = input("Encryption Type (Microsoft.Storage): ") or "Microsoft.Storage"
#         return {
#             "mode": "new",
#             "name": name,
#             "location": location,
#             "kind": kind,
#             "sku": sku,
#             "accessTier": tier,
#             "publicNetworkAccess": network,
#             "minimumTlsVersion": tls,
#             "encryptionType": encryption
#         }

#     # ======================================================
#     # Log Analytics Workspace
#     # ======================================================
#     def workspace(self):
#         print("\n==============================")
#         print("LOG ANALYTICS WORKSPACE")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Workspace Name: ")
#             return {"mode": "existing", "name": name}
#         name = input("Workspace Name: ")
#         location = input("Workspace Location: ")
#         return {"mode": "new", "name": name, "location": location}

#     # ======================================================
#     # Application Insights
#     # ======================================================
#     def application_insights(self):
#         print("\n==============================")
#         print("APPLICATION INSIGHTS")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Application Insights Name: ")
#             return {"mode": "existing", "name": name}
#         name = input("Application Insights Name: ")
#         location = input("Application Insights Location: ")
#         return {"mode": "new", "name": name, "location": location}

#     # ======================================================
#     # Function App - Flex Consumption
#     # ======================================================
#     def function_app(self):
#         print("\n==============================")
#         print("FUNCTION APP (Flex Consumption)")
#         print("==============================")
#         name = input("Function App Name: ")
#         location = input("Region (Location): ") or "eastus"
#         runtime_stack = input(
# "Runtime Stack (python,node,dotnet,java): "
# ).strip().lower() or "python"
#         runtime_version = input("Runtime Version (e.g. 3.11, 20, 8.0, ~4): ") or "3.11"
#         public_network = input("Public Network Access (Enabled/Disabled): ") or "Enabled"
#         enable_openai = input("Enable Azure OpenAI (true/false): ").lower() == "true"

#         # Hosting Plan for Flex Consumption
#         hosting_plan_name = input("Hosting Plan Name (press Enter for auto): ") or f"{name}-plan"

#         return {
#             "name": name,
#             "location": location,
#             "runtimeStack": runtime_stack,
#             "runtimeVersion": runtime_version,
#             "publicNetworkAccess": public_network,
#             "enableOpenAI": enable_openai,
#             "hostingPlanName": hosting_plan_name
#         }

#     # ======================================================
#     # Create parameters.json
#     # ======================================================
#     def create_parameter_file(self, rg, storage, app, workspace, func):
#         parameters = {
#             # Storage
#             "storageMode": {"value": storage["mode"]},
#             "storageAccountName": {"value": storage.get("name", "")},
#             "storageLocation": {"value": storage.get("location", rg["location"])},
#             "storageKind": {"value": storage.get("kind", "StorageV2")},
#             "storageSku": {"value": storage.get("sku", "Standard_LRS")},
#             "accessTier": {"value": storage.get("accessTier", "Hot")},
#             "publicNetworkAccess": {"value": storage.get("publicNetworkAccess", "Enabled")},
#             "minimumTlsVersion": {"value": storage.get("minimumTlsVersion", "TLS1_2")},
#             "encryptionType": {"value": storage.get("encryptionType", "Microsoft.Storage")},

#             # Workspace
#             "workspaceMode": {"value": workspace["mode"]},
#             "workspaceName": {"value": workspace.get("name", "")},
#             "workspaceLocation": {"value": workspace.get("location", rg["location"])},

#             # Application Insights
#             "appInsightsMode": {"value": app["mode"]},
#             "appInsightsName": {"value": app.get("name", "")},
#             "appInsightsLocation": {"value": app.get("location", rg["location"])},

#             # Function App - Flex Consumption
#             "functionAppMode": {"value": "new"},
#             "functionAppName": {"value": func["name"]},
#             "functionAppLocation": {"value": func.get("location", rg["location"])},
#             "functionRuntimeStack": {"value": func["runtimeStack"]},
#             "functionRuntimeVersion": {"value": func["runtimeVersion"]},
#             "functionPublicNetworkAccess": {"value": func["publicNetworkAccess"]},
#             "enableAzureOpenAI": {"value": func["enableOpenAI"]},
#             "hostingPlanName": {"value": func["hostingPlanName"]}
#         }

#         data = {
#             "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
#             "contentVersion": "1.0.0.0",
#             "parameters": parameters
#         }

#         file = (self.generated_folder / "parameters.json")
#         with open(file, "w") as f:
#             json.dump(data, f, indent=4)
#         print("\nGenerated parameters.json")
#         print(json.dumps(data, indent=4))
#         return file

#     # ======================================================
#     # ARM Deployment
#     # ======================================================
#     def deploy_template(self, rg_name, parameter_file):
#         command = [
#             "az",
#             "deployment",
#             "group",
#             "create",
#             "--resource-group",
#             rg_name,
#             "--template-file",
#             str(self.template_folder / "maintemplates.json"),
#             "--parameters",
#             f"@{parameter_file}"
#         ]
#         result = self.execute(command)
#         if result.returncode != 0:
#             raise Exception("ARM Deployment Failed")
#         print("\nARM Deployment Successful")

#     # ======================================================
#     # Run
#     # ======================================================
#     def run(self):
#         rg = self.resource_group()
#         storage = self.storage_account()
#         workspace = self.workspace()
#         app = self.application_insights()
#         func = self.function_app()

#         parameter_file = self.create_parameter_file(rg, storage, app, workspace, func)
#         self.deploy_template(rg["name"], parameter_file)


# # ======================================================
# # Main
# # ======================================================
# if __name__ == "__main__":
#     try:
#         deployment = AzureDeployment()
#         deployment.run()
#     except Exception as e:
#         print("\nDeployment Failed")
#         print(e)


# import json
# import subprocess
# from pathlib import Path
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import ResourceManagementClient
# from azure.core.exceptions import ResourceNotFoundError


# class AzureDeployment:
#     # ======================================================
#     # Constructor
#     # ======================================================
#     def __init__(self):
#         self.subscription_id = input("Subscription ID: ")
#         self.credential = DefaultAzureCredential()
#         self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)
#         self.template_folder = Path("templates")
#         self.generated_folder = Path("generated")
#         self.generated_folder.mkdir(exist_ok=True)

#     # ======================================================
#     # Execute Azure CLI
#     # ======================================================
#     def execute(self, command):
#         print("\n================================")
#         print("Executing")
#         print("================================\n")
#         print(" ".join(command))
#         result = subprocess.run(command, capture_output=True, text=True, shell=True)
#         print("\nSTDOUT")
#         print(result.stdout)
#         print("\nSTDERR")
#         print(result.stderr)
#         return result

#     # ======================================================
#     # Resource Group
#     # ======================================================
#     def resource_group(self):
#         print("\n==============================")
#         print("RESOURCE GROUP")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Resource Group Name: ")
#             try:
#                 rg = self.resource_client.resource_groups.get(name)
#                 print("\nUsing Existing Resource Group")
#                 return {"name": rg.name, "location": rg.location, "mode": "existing"}
#             except ResourceNotFoundError:
#                 raise Exception("Resource Group not found")
#         else:
#             name = input("New Resource Group Name: ")
#             location = input("Location: ")
#             self.resource_client.resource_groups.create_or_update(name, {"location": location})
#             print("\nResource Group Created")
#             return {"name": name, "location": location, "mode": "new"}

#     # ======================================================
#     # Storage Account
#     # ======================================================
#     def storage_account(self):
#         print("\n==============================")
#         print("STORAGE ACCOUNT")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Storage Account Name: ")
#             return {"mode": "existing", "name": name}
#         name = input("Storage Account Name: ")
#         location = input("Storage Location: ")
#         kind = input("Kind (StorageV2): ") or "StorageV2"
#         sku = input("SKU (Standard_LRS): ") or "Standard_LRS"
#         tier = input("Access Tier (Hot/Cool): ") or "Hot"
#         network = input("Public Network Access (Enabled/Disabled): ") or "Enabled"
#         tls = input("Minimum TLS Version (TLS1_2): ") or "TLS1_2"
#         encryption = input("Encryption Type (Microsoft.Storage): ") or "Microsoft.Storage"
#         return {
#             "mode": "new",
#             "name": name,
#             "location": location,
#             "kind": kind,
#             "sku": sku,
#             "accessTier": tier,
#             "publicNetworkAccess": network,
#             "minimumTlsVersion": tls,
#             "encryptionType": encryption
#         }

#     # ======================================================
#     # Log Analytics Workspace
#     # ======================================================
#     def workspace(self):
#         print("\n==============================")
#         print("LOG ANALYTICS WORKSPACE")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Workspace Name: ")
#             return {"mode": "existing", "name": name}
#         name = input("Workspace Name: ")
#         location = input("Workspace Location: ")
#         return {"mode": "new", "name": name, "location": location}

#     # ======================================================
#     # Application Insights
#     # ======================================================
#     def application_insights(self):
#         print("\n==============================")
#         print("APPLICATION INSIGHTS")
#         print("==============================")
#         mode = input("New or Existing (new/existing): ").lower()
#         if mode == "existing":
#             name = input("Existing Application Insights Name: ")
#             return {"mode": "existing", "name": name}
#         name = input("Application Insights Name: ")
#         location = input("Application Insights Location: ")
#         return {"mode": "new", "name": name, "location": location}

#     # ======================================================
#     # Function App - Flex Consumption
#     # ======================================================
#     def function_app(self):
#         print("\n==============================")
#         print("FUNCTION APP (Flex Consumption)")
#         print("==============================")
#         name = input("Function App Name: ")
#         location = input("Region (Location): ") or "eastus"
#         runtime_stack = input("Runtime Stack (python,node,dotnet,java): ").strip().lower() or "python"
#         runtime_version = input("Runtime Version (e.g. 3.11, 20, 8.0, ~4): ") or "3.11"
#         public_network = input("Public Network Access (Enabled/Disabled): ") or "Enabled"
#         enable_openai = input("Enable Azure OpenAI (true/false): ").lower() == "true"

#         hosting_plan_name = input("Hosting Plan Name (press Enter for auto): ") or f"{name}-plan"

#         return {
#             "name": name,
#             "location": location,
#             "runtimeStack": runtime_stack,
#             "runtimeVersion": runtime_version,
#             "publicNetworkAccess": public_network,
#             "enableOpenAI": enable_openai,
#             "hostingPlanName": hosting_plan_name
#         }

#     # ======================================================
#     # Logic App (Consumption)
#     # ======================================================
#     def logic_app(self):
#         print("\n==============================")
#         print("LOGIC APP (Consumption)")
#         print("==============================")
#         name = input("Logic App Name: ")
#         location = input("Region (Location): ") or "eastus"
#         enable_log_analytics = input("Enable Log Analytics (true/false): ").lower() == "true"
#         # Consumption Logic Apps are Stateful only
#         return {
#     "name": name,
#     "location": location,
#     "enableLogAnalytics": enable_log_analytics
# }

#     # ======================================================
#     # Create parameters.json
#     # ======================================================
#     def create_parameter_file(self, rg, storage, app, workspace, func, logic):
#         parameters = {
#             # Storage
#             "storageMode": {"value": storage["mode"]},
#             "storageAccountName": {"value": storage.get("name", "")},
#             "storageLocation": {"value": storage.get("location", rg["location"])},
#             "storageKind": {"value": storage.get("kind", "StorageV2")},
#             "storageSku": {"value": storage.get("sku", "Standard_LRS")},
#             "accessTier": {"value": storage.get("accessTier", "Hot")},
#             "publicNetworkAccess": {"value": storage.get("publicNetworkAccess", "Enabled")},
#             "minimumTlsVersion": {"value": storage.get("minimumTlsVersion", "TLS1_2")},
#             "encryptionType": {"value": storage.get("encryptionType", "Microsoft.Storage")},

#             # Workspace
#             "workspaceMode": {"value": workspace["mode"]},
#             "workspaceName": {"value": workspace.get("name", "")},
#             "workspaceLocation": {"value": workspace.get("location", rg["location"])},

#             # Application Insights
#             "appInsightsMode": {"value": app["mode"]},
#             "appInsightsName": {"value": app.get("name", "")},
#             "appInsightsLocation": {"value": app.get("location", rg["location"])},

#             # Function App
#             "functionAppMode": {"value": "new"},
#             "functionAppName": {"value": func["name"]},
#             "functionAppLocation": {"value": func.get("location", rg["location"])},
#             "functionRuntimeStack": {"value": func["runtimeStack"]},
#             "functionRuntimeVersion": {"value": func["runtimeVersion"]},
#             "functionPublicNetworkAccess": {"value": func["publicNetworkAccess"]},
#             "enableAzureOpenAI": {"value": func["enableOpenAI"]},
#             "hostingPlanName": {"value": func["hostingPlanName"]},

#             # Logic App
#             "logicAppMode": {"value": "new"},
#             "logicAppName": {"value": logic["name"]},
#             "logicAppLocation": {"value": logic.get("location", rg["location"])},
#             "enableLogAnalytics": {"value": logic["enableLogAnalytics"]},
            
#         }

#         data = {
#             "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
#             "contentVersion": "1.0.0.0",
#             "parameters": parameters
#         }

#         file = (self.generated_folder / "parameters.json")
#         with open(file, "w") as f:
#             json.dump(data, f, indent=4)
#         print("\nGenerated parameters.json")
#         print(json.dumps(data, indent=4))
#         return file

#     # ======================================================
#     # ARM Deployment
#     # ======================================================
#     def deploy_template(self, rg_name, parameter_file):
#         command = [
#             "az",
#             "deployment",
#             "group",
#             "create",
#             "--resource-group",
#             rg_name,
#             "--template-file",
#             str(self.template_folder / "maintemplates.json"),
#             "--parameters",
#             f"@{parameter_file}"
#         ]
#         result = self.execute(command)
#         if result.returncode != 0:
#             raise Exception("ARM Deployment Failed")
#         print("\nARM Deployment Successful")

#     # ======================================================
#     # Run
#     # ======================================================
#     def run(self):
#         rg = self.resource_group()
#         storage = self.storage_account()
#         workspace = self.workspace()
#         app = self.application_insights()
#         func = self.function_app()
#         logic = self.logic_app()   # <-- Added

#         parameter_file = self.create_parameter_file(rg, storage, app, workspace, func, logic)
#         self.deploy_template(rg["name"], parameter_file)


# # ======================================================
# # Main
# # ======================================================
# if __name__ == "__main__":
#     try:
#         deployment = AzureDeployment()
#         deployment.run()
#     except Exception as e:
#         print("\nDeployment Failed")
#         print(e)

import json
import subprocess
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceNotFoundError


class AzureDeployment:

    # ======================================================
    # Constructor
    # ======================================================
    def __init__(self, payload):

        self.payload = payload

        self.subscription_id = payload["subscriptionId"]

        self.credential = DefaultAzureCredential()

        self.resource_client = ResourceManagementClient(
            self.credential,
            self.subscription_id
        )

        self.template_folder = Path("templates")

        self.generated_folder = Path("generated")
        self.generated_folder.mkdir(exist_ok=True)


    # ======================================================
    # Execute Azure CLI
    # ======================================================
    def execute(self, command):

        print("\n================================")
        print("Executing Deployment")
        print("================================\n")

        print(" ".join(command))

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True
        )

        print("\nSTDOUT")
        print(result.stdout)

        print("\nSTDERR")
        print(result.stderr)

        return result


    # ======================================================
    # Resource Group
    # ======================================================
    def resource_group(self):

        rg = self.payload["resourceGroup"]

        if rg["mode"] == "existing":

            try:

                resource_group = self.resource_client.resource_groups.get(
                    rg["name"]
                )

                return {
                    "name": resource_group.name,
                    "location": resource_group.location,
                    "mode": "existing"
                }


            except ResourceNotFoundError:

                raise Exception(
                    "Resource Group does not exist"
                )


        else:

            self.resource_client.resource_groups.create_or_update(
                rg["name"],
                {
                    "location": rg["location"]
                }
            )


            return {

                "name": rg["name"],
                "location": rg["location"],
                "mode": "new"

            }


    # ======================================================
    # Storage Account
    # ======================================================
    def storage_account(self):

        return self.payload["storage"]



    # ======================================================
    # Log Analytics Workspace
    # ======================================================
    def workspace(self):

        return self.payload["workspace"]



    # ======================================================
    # Application Insights
    # ======================================================
    def application_insights(self):

        return self.payload["applicationInsights"]



    # ======================================================
    # Function App
    # ======================================================
    def function_app(self):

        return self.payload["functionApp"]



    # ======================================================
    # Logic App
    # ======================================================
    def logic_app(self):

        return self.payload["logicApp"]



    # ======================================================
    # Create parameters.json
    # ======================================================
    def create_parameter_file(
            self,
            rg,
            storage,
            app,
            workspace,
            func,
            logic
    ):


        parameters = {


            # -------------------------
            # Storage
            # -------------------------

            "storageMode":
            {
                "value": storage["mode"]
            },


            "storageAccountName":
            {
                "value": storage["name"]
            },


            "storageLocation":
            {
                "value": storage.get(
                    "location",
                    rg["location"]
                )
            },


            "storageKind":
            {
                "value": storage.get(
                    "kind",
                    "StorageV2"
                )
            },


            "storageSku":
            {
                "value": storage.get(
                    "sku",
                    "Standard_LRS"
                )
            },


            "accessTier":
            {
                "value": storage.get(
                    "accessTier",
                    "Hot"
                )
            },


            "publicNetworkAccess":
            {
                "value": storage.get(
                    "publicNetworkAccess",
                    "Enabled"
                )
            },


            "minimumTlsVersion":
            {
                "value": storage.get(
                    "minimumTlsVersion",
                    "TLS1_2"
                )
            },


            "encryptionType":
            {
                "value": storage.get(
                    "encryptionType",
                    "Microsoft.Storage"
                )
            },



            # -------------------------
            # Workspace
            # -------------------------

            "workspaceMode":
            {
                "value": workspace["mode"]
            },


            "workspaceName":
            {
                "value": workspace["name"]
            },


            "workspaceLocation":
            {
                "value": workspace.get(
                    "location",
                    rg["location"]
                )
            },



            # -------------------------
            # Application Insights
            # -------------------------

            "appInsightsMode":
            {
                "value": app["mode"]
            },


            "appInsightsName":
            {
                "value": app["name"]
            },


            "appInsightsLocation":
            {
                "value": app.get(
                    "location",
                    rg["location"]
                )
            },



            # -------------------------
            # Function App
            # -------------------------

            "functionAppMode":
            {
                "value": "new"
            },


            "functionAppName":
            {
                "value": func["name"]
            },


            "functionAppLocation":
            {
                "value": func.get(
                    "location",
                    rg["location"]
                )
            },


            "functionRuntimeStack":
            {
                "value": func["runtimeStack"]
            },


            "functionRuntimeVersion":
            {
                "value": func["runtimeVersion"]
            },


            "functionPublicNetworkAccess":
            {
                "value": func.get(
                    "publicNetworkAccess",
                    "Enabled"
                )
            },


            "enableAzureOpenAI":
            {
                "value": func.get(
                    "enableOpenAI",
                    False
                )
            },


            "hostingPlanName":
            {
                "value": func["hostingPlanName"]
            },



            # -------------------------
            # Logic App
            # -------------------------

            "logicAppMode":
            {
                "value": "new"
            },


            "logicAppName":
            {
                "value": logic["name"]
            },


            "logicAppLocation":
            {
                "value": logic.get(
                    "location",
                    rg["location"]
                )
            },


            "enableLogAnalytics":
            {
                "value": logic.get(
                    "enableLogAnalytics",
                    False
                )
            }

        }



        data = {

            "$schema":
            "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",


            "contentVersion":
            "1.0.0.0",


            "parameters":
            parameters

        }



        file = (
            self.generated_folder /
            "parameters.json"
        )


        with open(file,"w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


        print("\nGenerated parameters.json")

        return file



    # ======================================================
    # ARM Deployment
    # ======================================================
    def deploy_template(
            self,
            rg_name,
            parameter_file
    ):


        command = [

            "az",
            "deployment",
            "group",
            "create",

            "--resource-group",
            rg_name,

            "--template-file",
            str(
                self.template_folder /
                "maintemplates.json"
            ),

            "--parameters",
            f"@{parameter_file}"

        ]


        result = self.execute(command)


        if result.returncode != 0:

            raise Exception(
                "ARM Deployment Failed"
            )


        return True



    # ======================================================
    # Main Run
    # ======================================================
    def run(self):


        rg = self.resource_group()

        storage = self.storage_account()

        workspace = self.workspace()

        app = self.application_insights()

        func = self.function_app()

        logic = self.logic_app()



        parameter_file = self.create_parameter_file(

            rg,

            storage,

            app,

            workspace,

            func,

            logic

        )



        self.deploy_template(

            rg["name"],

            parameter_file

        )


        return {

            "status": "success",

            "resourceGroup":
            rg["name"]

        }



# ======================================================
# Example execution
# ======================================================

if __name__ == "__main__":


    payload = {

        # This will come from API later

    }


    deployment = AzureDeployment(payload)

    response = deployment.run()

    print(response)