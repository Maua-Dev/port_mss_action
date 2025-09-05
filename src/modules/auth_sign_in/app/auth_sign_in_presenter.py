from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .auth_sign_in_controller import AuthSignInController
from .auth_sign_in_usecase import AuthSignInUsecase

env = Environments.get_instance()
usecase = AuthSignInUsecase(client_id=env.cognito_client_id, region=env.region)
controller = AuthSignInController(usecase=usecase)

def auth_sign_in_presenter(event, _context):
    req = LambdaHttpRequest(data=event)
    resp = controller(req)
    http = LambdaHttpResponse(status_code=resp.status_code, body=resp.body, headers=resp.headers)
    return http.toDict()

def lambda_handler(event, context):
    return auth_sign_in_presenter(event, context)
