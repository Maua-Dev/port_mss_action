from .get_all_actions_by_ra_usecase import GetAllActionsByRaUsecase
from .get_all_actions_by_ra_viewmodel import GetAllActionsByRaViewmodel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter

class GetAllActionsByRaController:
    
    def __init__(self, usecase: GetAllActionsByRaUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('ra') is None:
                raise MissingParameters('ra')
            
            actions = self.usecase(ra=request.data.get('ra'))
            viewmodel = GetAllActionsByRaViewmodel(associated_actions=actions, ra=request.data.get('ra'))
            
            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
            
        except Exception as err:
            return InternalServerError(body=err.args[0])