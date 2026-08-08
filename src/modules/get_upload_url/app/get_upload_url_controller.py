from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, ForbiddenAction
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_upload_url_usecase import GetUploadUrlUsecase
from .get_upload_url_viewmodel import GetUploadUrlViewModel

class GetUploadUrlController:
    def __init__(self, usecase: GetUploadUrlUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            if request.data.get('file_name') is None:
                raise MissingParameters('file_name')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            url = self.usecase(
                user_id=requester_user.user_id,
                file_name=request.data.get('file_name'),
            )

            viewmodel = GetUploadUrlViewModel(url=url)
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)
        except EntityError as err:
            return BadRequest(body=err.message)
        except UnregisteredUser as err:
            return Forbidden(body=err.message)
        except ForbiddenAction as err:
            return Forbidden(body=err.message)
        except Exception as err:
            return InternalServerError(body=err.args[0])