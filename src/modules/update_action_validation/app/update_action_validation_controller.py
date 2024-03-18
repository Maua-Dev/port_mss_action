from .update_action_validation_usecase import UpdateActionValidationUsecase
from .update_action_validation_viewmodel import UpdateActionValidationViewModel
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UserNotAllowed, NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class UpdateActionValidationController:
    
    def __init__(self, use_case: UpdateActionValidationUsecase):
        self.UpdateActionValidationUsecase = use_case

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if request.data.get('action_id') is None:
                raise MissingParameters('action_id')
            
            if request.data.get('is_valid') is None:
                raise MissingParameters('is_valid')
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            action_validation = self.UpdateActionValidationUsecase(
                action_id = str(request.data.get('action_id')),
                new_is_valid = bool(request.data.get('is_valid')),
                user_id = str(requester_user.user_id) if requester_user is not None else None
            )

            viewmodel = UpdateActionValidationViewModel(action_id = action_validation.action_id, is_valid = action_validation.is_valid, user_id = requester_user.user_id if requester_user is not None else None)

            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except UserNotAllowed as err:
            return NotFound(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])