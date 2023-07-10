from .create_project_controller import CreateProjectController
from .create_project_usecase import CreateProjectUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_action_repo()()
usecase = CreateProjectUsecase(repo=repo)
controller = CreateProjectController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()