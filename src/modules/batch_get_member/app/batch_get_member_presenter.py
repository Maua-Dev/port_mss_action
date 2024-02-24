from .batch_get_member_usecase import BatchGetMemberUsecase
from .batch_get_member_controller import BatchGetMemberController
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_member_repo()()
usecase = BatchGetMemberUsecase(repo=repo)
controller = BatchGetMemberController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()