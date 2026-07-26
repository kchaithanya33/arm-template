import subprocess
from pathlib import Path
import uuid



class ARMDeployment:


    def __init__(self):

        self.base_path = Path(__file__).parent


        self.rg_template_path = (
            self.base_path
            /
            "templates"
            /
            "subscription-create-rg.json"
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
    # Subscription Scope
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
# Wrapper Function
# ==================================================

def create_resource_group_template(

        location,

        parameter_file

):


    deployment = ARMDeployment()


    return deployment.create_resource_group(

        location,

        parameter_file

    )