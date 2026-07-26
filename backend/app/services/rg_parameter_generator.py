import json

from pathlib import Path



# ======================================================
# Generate Resource Group ARM Parameters
# ======================================================

def generate_rg_parameters_file(resource_group):


    # Only required for new RG

    if resource_group.mode != "new":

        raise ValueError(
            "Parameters required only for new Resource Group"
        )


    if not resource_group.name:

        raise ValueError(
            "Resource Group name is required"
        )


    if not resource_group.location:

        raise ValueError(
            "Resource Group location is required"
        )



    # ARM parameter structure

    parameters = {


        "$schema":
        "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",


        "contentVersion":
        "1.0.0.0",


        "parameters":{


            "resourceGroupName":{

                "value":
                resource_group.name

            },


            "resourceGroupLocation":{

                "value":
                resource_group.location

            }

        }

    }



    # Create folder

    output_folder = Path(
        "arm/generated"
    )


    output_folder.mkdir(
        exist_ok=True
    )



    file_path = (
        output_folder /
        "rg_parameters.json"
    )



    # Write JSON

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