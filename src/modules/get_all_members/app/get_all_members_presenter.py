from .get_all_members_controller import GetAllMembersController
from .get_all_members_usecase import GetAllMembersUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


memberrepo = Environments.get_member_repo()()
actionrepo = Environments.get_action_repo()()
usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
controller = GetAllMembersController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()