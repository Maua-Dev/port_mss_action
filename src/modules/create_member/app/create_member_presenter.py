from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from .create_member_controller import CreateMemberController
from .create_member_usecase import CreateMemberUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
    
repo = Environments.get_member_repo()()
usecase = CreateMemberUsecase(repo=repo)
controller = CreateMemberController(usecase=usecase)


def create_member_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = create_member_presenter(event, context)
   
    return response