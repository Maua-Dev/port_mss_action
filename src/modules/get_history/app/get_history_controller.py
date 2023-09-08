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
            if request.data.get('ra') is None:
                raise MissingParameters('ra')
            if type(request.data.get('ra')) is not str:
                raise WrongTypeParameter(fieldName='ra', fieldTypeExpected='str', fieldTypeReceived=type(request.data.get('ra')))
            if not Member.validate_ra(request.data.get('ra')):
                raise EntityError('ra')
            
            if request.data.get('start') is not None:
                if type(request.data.get('start')) is not str:
                    raise WrongTypeParameter(fieldName='start', fieldTypeExpected='str', fieldTypeReceived=type(request.data.get('start')))
                if not request.data.get('start').isdecimal():
                    raise EntityError('start')
                if not 1000000000000 < int(request.data.get('start')) < 10000000000000:
                    raise EntityError('start')
                start = int(request.data.get('start'))
            else:
                start = None
            
            if request.data.get('end') is not None:
                if type(request.data.get('end')) is not str:
                    raise WrongTypeParameter(fieldName='end', fieldTypeExpected='str', fieldTypeReceived=type(request.data.get('end')))
                if not request.data.get('end').isdecimal():
                    raise EntityError('end')
                if not 1000000000000 < int(request.data.get('end')) < 10000000000000:
                    raise EntityError('end')
                end = int(request.data.get('end'))
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
                if type(request.data.get('amount')) is not str:
                    raise WrongTypeParameter(fieldName='amount', fieldTypeExpected='str', fieldTypeReceived=type(request.data.get('amount')))
                if not request.data.get('amount').isdecimal():
                    raise EntityError('amount')
                amount = int(request.data.get('amount'))
                if amount < 1:
                    raise EntityError('amount')
            else:
                amount = None
                
            actions, last_evaluated_key = self.usecase(ra=request.data.get('ra'), start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)

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