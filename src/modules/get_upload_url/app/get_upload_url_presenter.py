from .get_upload_url_usecase import GetUploadUrlUsecase
from .get_upload_url_controller import GetUploadUrlController
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.infra.repositories.S3Manager import S3Manager

member_repo = Environments.get_member_repo()()
s3_manager = S3Manager()
usecase = GetUploadUrlUsecase(member_repo=member_repo, s3_manager=s3_manager)
controller = GetUploadUrlController(usecase=usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    httpRequest.data['file_name'] = event.get('queryStringParameters', {}).get('file_name', None)

    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code,
        body=response.body,
        headers=response.headers
    )
    return httpResponse.toDict()