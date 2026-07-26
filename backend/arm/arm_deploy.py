import subprocess
from pathlib import Path
import uuid



class ARMDeployment:


    def __init__(self):


        self.base_path = Path(__file__).parent



        # ==================================================
        # Subscription Scope Template
        # Used for creating Resource Group
        # ==================================================

        self.rg_template_path = (

            self.base_path

            /

            "templates"

            /

            "subscription-create-rg.json"

        )



        # ==================================================
        # Resource Group Scope Template
        # Used for Storage Account and other resources
        # ==================================================

        self.resource_template_path = (

            self.base_path

            /

            "templates"

            /

            "maintemplates.json"

        )





    # ==================================================
    # Execute Azure CLI Command
    # ==================================================

    def execute(self, command):


        print("\n======================")

        print("AZURE COMMAND")

        print("======================")



        print(" ".join(command))



        result = subprocess.run(

            command,

            capture_output=True,

            text=True,

            shell=True

        )



        print(result.stdout)

        print(result.stderr)



        return result





    # ==================================================
    # CREATE RESOURCE GROUP
    #
    # Subscription Scope Deployment
    #
    # Command:
    # az deployment sub create
    #
    # ==================================================

    def create_resource_group(

            self,

            location,

            parameter_file

    ):


        deployment_name = (

            f"rg-deployment-{uuid.uuid4()}"

        )



        command = [


            "az",


            "deployment",


            "sub",


            "create",



            "--name",


            deployment_name,



            "--location",


            location,



            "--template-file",


            str(self.rg_template_path),



            "--parameters",


            f"@{parameter_file}"


        ]



        result = self.execute(command)



        if result.returncode != 0:


            raise Exception(

                result.stderr

            )



        return {


            "status": "success",


            "message": "Resource Group created",


            "deploymentName": deployment_name


        }







    # ==================================================
    # DEPLOY RESOURCES INSIDE RESOURCE GROUP
    #
    # Resource Group Scope Deployment
    #
    # Command:
    # az deployment group create
    #
    # Used for:
    # - Storage Account
    # - App Service Plan
    # - Function App
    # - Logic App
    #
    # ==================================================

    def deploy_resource_group_resources(

            self,

            resource_group_name,

            parameter_file

    ):



        deployment_name = (

            f"resource-deployment-{uuid.uuid4()}"

        )



        command = [



            "az",



            "deployment",



            "group",



            "create",




            "--name",



            deployment_name,




            "--resource-group",



            resource_group_name,




            "--template-file",



            str(self.resource_template_path),




            "--parameters",



            f"@{parameter_file}"


        ]



        result = self.execute(command)



        if result.returncode != 0:


            raise Exception(

                result.stderr

            )



        return {


            "status": "success",


            "message": "Resource deployment completed",


            "deploymentName": deployment_name


        }





# ======================================================
# Wrapper Function
# ======================================================


def create_resource_group_template(

        location,

        parameter_file

):


    deployment = ARMDeployment()



    return deployment.create_resource_group(

        location,

        parameter_file

    )






# ======================================================
# Wrapper Function
# ======================================================

def create_resource_group_deployment(

        resource_group_name,

        parameter_file

):


    deployment = ARMDeployment()



    return deployment.deploy_resource_group_resources(

        resource_group_name,

        parameter_file

    )