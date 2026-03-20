from .get_strike_usecase import GetStrikeUsecase
from .get_strike_viewmodel import GetStrikeViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, UserNotAllowed
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

class GetStrikeController:

    def __init__(self, usecase: GetStrikeUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            # Validação do parâmetro de entrada
            if request.data.get('strike_id') is None:
                raise MissingParameters('strike_id')

            # Validação do usuário do token
            requester_user = request.data.get('requester_user')
            if requester_user is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(requester_user)

            strike_id= request.data.get('strike_id')

            if type(strike_id) is not str:
                raise WrongTypeParameter('strike_id', 'str', type(strike_id))

            # Execução do caso de uso
            strike = self.usecase(
                strike_id=strike_id,
                user_id=requester_user.user_id
            )

            # Criação do View Model
            viewmodel = GetStrikeViewmodel(strike=strike)
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except UnregisteredUser as err:
            return Forbidden(body=err.message)

        except UserNotAllowed as err:
            return Forbidden(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])