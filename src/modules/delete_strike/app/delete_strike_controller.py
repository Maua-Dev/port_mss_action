from src.modules.delete_strike.app.delete_strike_viewmodel import DeleteStrikeViewModel
from src.shared.domain.entities.strike import Strike
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_strike_usecase import DeleteStrikeUseCase

class DeleteStrikeController:
    def __init__(self, usecase: DeleteStrikeUseCase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('strike_id') is None:
                raise MissingParameters('strike_id')
            if not Strike.validate_strike_id(request.data.get('strike_id')):
                raise EntityError('strike_id')

            strike_id = request.data.get('strike_id')
            strike = self.DeleteStrikeUseCase(user_id=requester_user.user_id, strike_id=strike_id)

            viewmodel = DeleteStrikeViewModel(strike)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])