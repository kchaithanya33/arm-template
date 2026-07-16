import json
import uuid
from pathlib import Path

from azure.mgmt.resource import ResourceManagementClient

from app.azure.auth import get_credential, get_subscription_id


# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

ARM_TEMPLATE_DIR = PROJECT_ROOT / "arm_templates"

TEMPLATE_FILE = ARM_TEMPLATE_DIR / "infrastructure.json"


# --------------------------------------------------
# Azure Resource Management Client
# --------------------------------------------------

client = ResourceManagementClient(
    credential=get_credential(),
    subscription_id=get_subscription_id()
)


# --------------------------------------------------
# Load ARM Template
# --------------------------------------------------

def load_template():
    """
    Loads the ARM template.
    """

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
        template = json.load(file)

    return template


# --------------------------------------------------
# Deploy ARM Template
# --------------------------------------------------

def deploy_template(resource_group_name: str, parameters: dict):
    """
    Deploys the ARM template to Azure.
    """

    template = load_template()

    deployment_name = f"deployment-{uuid.uuid4().hex[:8]}"

    deployment_properties = {
        "properties": {
            "mode": "Incremental",
            "template": template,
            "parameters": parameters["parameters"]
        }
    }

    print(f"\nStarting Deployment: {deployment_name}")

    poller = client.deployments.begin_create_or_update(
        resource_group_name=resource_group_name,
        deployment_name=deployment_name,
        parameters=deployment_properties
    )

    result = poller.result()

    return {
        "deploymentName": deployment_name,
        "status": result.properties.provisioning_state
    }


# --------------------------------------------------
# Temporary Test
# --------------------------------------------------

if __name__ == "__main__":

    from app.deployment.schemas import DeploymentRequest
    from app.deployment.parameter_generator import generate_parameters

    request = DeploymentRequest(

        resourceGroup="arm-functionapp-test-rg",

        location="Central India",

        storageAccountName="sdkstorage12345",

        applicationInsightsName="sdk-ai-12345",

        appServicePlanName="sdk-plan-12345",

        functionAppName="sdk-function-12345",

        logicAppName="sdk-logic-12345"

    )

    parameters = generate_parameters(request)

    response = deploy_template(
        resource_group_name=request.resourceGroup,
        parameters=parameters
    )

    print("\nDeployment Result")
    print(response)