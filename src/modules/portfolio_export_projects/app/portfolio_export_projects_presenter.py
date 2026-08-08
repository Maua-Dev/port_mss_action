from .portfolio_export_projects_usecase import PortfolioExportProjectsUsecase
from .portfolio_export_projects_controller import PortfolioExportProjectsController
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

action_repo = Environments.get_action_repo()()

usecase = PortfolioExportProjectsUsecase(action_repo=action_repo)
controller = PortfolioExportProjectsController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)

    response = controller(httpRequest)

    httpResponse = LambdaHttpResponse(
        status_code=response.status_code,
        body=response.body,
        headers=response.headers
    )

    return httpResponse.toDict()
