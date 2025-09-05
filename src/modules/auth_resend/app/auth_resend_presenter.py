from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .auth_resend_controller import AuthResendController
from .auth_resend_usecase import AuthResendUsecase

env = Environments.get_instance()
usecase = AuthResendUsecase(client_id=env.cognito_client_id, region=env.region)
controller = AuthResendController(usecase=usecase)

def auth_resend_presenter(event, _context):
    req = LambdaHttpRequest(data=event)
    resp = controller(req)
    http = LambdaHttpResponse(status_code=resp.status_code, body=resp.body, headers=resp.headers)
    return http.toDict()

def lambda_handler(event, context):
    return auth_resend_presenter(event, context)
