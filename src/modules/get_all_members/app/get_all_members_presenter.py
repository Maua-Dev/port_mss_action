from .get_all_members_controller import GetAllMembersController
from .get_all_members_usecase import GetAllMembersUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_member_repo()()
usecase = GetAllMembersUsecase(repo=repo)
controller = GetAllMembersController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()