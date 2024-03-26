from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_history_usecase import GetHistoryUsecase
from .get_history_viewmodel import GetHistoryViewmodel
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound

class GetHistoryController:
    
    def __init__(self, usecase: GetHistoryUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if type(requester_user.user_id) is not str:
                raise WrongTypeParameter(fieldName='user_id', fieldTypeExpected='str', fieldTypeReceived=type(requester_user.user_id))
            if not Member.validate_user_id(requester_user.user_id):
                raise EntityError('user_id')
            
            if request.data.get('start') is not None:
                if type(request.data.get('start')) is not int:
                    raise WrongTypeParameter(fieldName='start', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('start')))
                if not 1000000000000 < request.data.get('start') < 10000000000000:
                    raise EntityError('start')
                start = request.data.get('start')
            else:
                start = None
            
            if request.data.get('end') is not None:
                if type(request.data.get('end')) is not int:
                    raise WrongTypeParameter(fieldName='end', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('end')))
                if not 1000000000000 < request.data.get('end') < 10000000000000:
                    raise EntityError('end')
                end = request.data.get('end')
            else:
                end = None

            if start is not None and end is not None:
                if start > end:
                    raise EntityError('start')
            
            if request.data.get('exclusive_start_key') is not None:
                if not AssociatedAction.validate_action_id(request.data.get('exclusive_start_key')["action_id"]):
                    raise EntityError('exclusive_start_key action_id')
                if not 1000000000000 < int(request.data.get('exclusive_start_key')["start_date"]) < 10000000000000:
                    raise EntityError('exclusive_start_key start_date')
                exclusive_start_key = {"action_id" : request.data.get('exclusive_start_key')["action_id"], "start_date" : int(request.data.get('exclusive_start_key')["start_date"])}
            else:
                exclusive_start_key = None
            
            if request.data.get('amount') is not None:
                if type(request.data.get('amount')) is not int:
                    raise WrongTypeParameter(fieldName='amount', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('amount')))
                amount = request.data.get('amount')
                if amount < 1:
                    raise EntityError('amount')
            else:
                amount = None
                
            actions, last_evaluated_key = self.usecase(user_id=requester_user.user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)

            viewmodel = GetHistoryViewmodel(actions=actions, last_evaluated_key=last_evaluated_key)
            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])