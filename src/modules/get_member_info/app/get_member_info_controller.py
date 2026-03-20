from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from .get_member_info_usecase import GetMemberInfoUsecase
from .get_member_info_viewmodel import GetMemberInfoViewModel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetMemberInfoController:
    def __init__(self, usecase: GetMemberInfoUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest):
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            print(f"Fetching member info for user_id: {requester_user.user_id}")

            member = self.usecase(user_id=requester_user.user_id)

            viewmodel = GetMemberInfoViewModel(member=member)

            print("Member info retrieved successfully")

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            print(f"Missing parameters error: {err.message}")
            return BadRequest(body=err.message)

        except EntityError as err:
            print(f"Entity error: {err.message}")
            return BadRequest(body=err.message)

        except UnregisteredUser as err:
            print(f"Unregistered user error: {err.message}")
            return Forbidden(body=err.message)

        except UserNotAllowed as err:
            print(f"User not allowed error: {err.message}")
            return Forbidden(body=err.message)

        except Exception as err:
            print(f"Unexpected error: {str(err)}")
            return InternalServerError(body=err.args[0])