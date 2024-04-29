from .delete_action_controller import DeleteActionController
from .delete_action_usecase import DeleteActionUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_action_repo()()
repo_member = Environments.get_member_repo()()
usecase =   DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
controller = DeleteActionController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()