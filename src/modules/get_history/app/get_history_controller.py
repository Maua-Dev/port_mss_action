from .get_history_usecase import GetHistoryUsecase
from .get_history_viewmodel import GetHistoryViewmodel
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class GetHistoryController:
    repo = ActionRepositoryMock()
    
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
                if type(request.data.get('start')) is not int:
                    raise WrongTypeParameter(fieldName='start', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('start')))
                if not 1000000000000 < request.data.get('start') < 10000000000000:
                    raise EntityError('start')
            if request.data.get('end') is not None:
                if type(request.data.get('end')) is not int:
                    raise WrongTypeParameter(fieldName='end', fieldTypeExpected='int', fieldTypeReceived=type(request.data.get('end')))
                if not 1000000000000 < request.data.get('end') < 10000000000000:
                    raise EntityError('end')
            if request.data.get('start') and request.data.get('end'):
                if request.data.get('start') > request.data.get('end'):
                    raise EntityError('start')
            
            if request.data.get('exclusive_start_key') is not None:
                if not AssociatedAction.validate_action_id(request.data.get('exclusive_start_key')):
                    raise EntityError('exclusive_start_key')
            
            if request.data.get('amount') is not None:
                if type(request.data.get('amount')) is not int:
                    raise WrongTypeParameter('amount', 'int', type(request.data.get('amount')))
                if request.data.get('amount') < 1:
                    raise EntityError('amount')
                
            actions, last_evaluated_key = self.usecase(ra=request.data.get('ra'), start=request.data.get('start'), end=request.data.get('end'), exclusive_start_key=request.data.get('exclusive_start_key'), amount=request.data.get('amount'))

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