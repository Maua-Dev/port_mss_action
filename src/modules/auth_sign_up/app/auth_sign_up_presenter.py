from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .auth_sign_up_controller import AuthSignUpController
from .auth_sign_up_usecase import AuthSignUpUsecase

env = Environments.get_instance()

usecase = AuthSignUpUsecase(client_id=env.cognito_client_id, region=env.region)
controller = AuthSignUpController(usecase=usecase)

def auth_sign_up_presenter(event, _context):
    req = LambdaHttpRequest(data=event)
    resp = controller(req)
    http = LambdaHttpResponse(status_code=resp.status_code, body=resp.body, headers=resp.headers)
    return http.toDict()

def lambda_handler(event, context):
    return auth_sign_up_presenter(event, context)
