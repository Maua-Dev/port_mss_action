from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .auth_confirm_controller import AuthConfirmController
from .auth_confirm_usecase import AuthConfirmUsecase

env = Environments.get_instance()
usecase = AuthConfirmUsecase(client_id=env.cognito_client_id, region=env.region)
controller = AuthConfirmController(usecase=usecase)

def auth_confirm_presenter(event, _context):
    req = LambdaHttpRequest(data=event)
    resp = controller(req)
    http = LambdaHttpResponse(status_code=resp.status_code, body=resp.body, headers=resp.headers)
    return http.toDict()

def lambda_handler(event, context):
    return auth_confirm_presenter(event, context)
