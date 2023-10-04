from .delete_member_controller import DeleteMemberController
from .delete_member_usecase import DeleteMemberUseCase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_action_repo()()
usecase =   DeleteMemberUseCase(repo=repo)
controller = DeleteMemberController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()