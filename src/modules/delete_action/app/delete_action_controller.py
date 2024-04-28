from src.shared.domain.entities.member import Member
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_action_usecase import DeleteActionUsecase
from .delete_action_viewmodel import DeleteActionViewModel
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError 
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class DeleteActionController:
    def __init__(self, usecase: DeleteActionUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            action_id = request.data.get('action_id')
            if action_id is None:
                raise MissingParameters('action_id')
            if type(action_id) is not str:
                raise WrongTypeParameter(fieldName='action_id')
            if not Action.validate_action_id(action_id):
                raise EntityError('action_id')
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if type(requester_user.user_id) is not str:
                raise WrongTypeParameter(fieldName='user_id', fieldTypeExpected='str', fieldTypeReceived=type(requester_user.user_id))
            if not Member.validate_user_id(requester_user.user_id):
                raise EntityError('user_id')
            
            action = self.usecase(action_id=action_id, user_id=requester_user.user_id)
            viewmodel = DeleteActionViewModel(action)

            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])