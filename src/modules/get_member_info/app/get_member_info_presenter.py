from .get_member_info_usecase import GetMemberInfoUsecase
from .get_member_info_controller import GetMemberInfoController
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

member_repo = Environments.get_member_repo()()
action_repo = Environments.get_action_repo()()

usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)
controller = GetMemberInfoController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)

    response = controller(httpRequest)

    httpResponse = LambdaHttpResponse(
        status_code=response.status_code,
        body=response.body,
        headers=response.headers
    )

    return httpResponse.toDict()