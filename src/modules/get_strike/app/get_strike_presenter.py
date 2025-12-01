from .get_strike_controller import GetStrikeController
from .get_strike_usecase import GetStrikeUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

# Atenção: Certifique-se que Environments possui o método get_strike_repo
repo_strike = Environments.get_strike_repo()()
repo_member = Environments.get_member_repo()()

usecase = GetStrikeUsecase(repo_strike=repo_strike, repo_member=repo_member)
controller = GetStrikeController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)

    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()