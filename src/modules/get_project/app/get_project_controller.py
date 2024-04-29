from .get_project_usecase import GetProjectUsecase
from .get_project_viewmodel import GetProjectViewmodel
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

class GetProjectController:
    
    def __init__(self, usecase: GetProjectUsecase):
        self.usecase = usecase
        
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('code') is None:
                raise MissingParameters('code')
            
            requester_user = request.data.get('requester_user')
            
            if requester_user is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(requester_user)
            
            project= self.usecase(request.data.get('code'), requester_user.user_id)
            viewmodel = GetProjectViewmodel(project=project)
            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])