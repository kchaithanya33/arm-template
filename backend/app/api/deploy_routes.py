from fastapi import APIRouter

from app.deployment.schemas import DeploymentRequest
from app.deployment.parameter_generator import generate_parameters
from app.deployment.arm_deployer import deploy_template

router = APIRouter(prefix="/deploy", tags=["Deployment"])


@router.post("/")
def deploy(request: DeploymentRequest):

    parameters = generate_parameters(request)

    result = deploy_template(
        resource_group_name=request.resourceGroup,
        parameters=parameters
    )

    return result