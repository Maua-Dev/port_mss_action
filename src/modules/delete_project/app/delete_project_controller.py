from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_project_usecase import DeleteProjectUsecase
from .delete_project_viewmodel import DeleteProjectViewModel
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound


class DeleteProjectController:
    
    def __init__(self, usecase:  DeleteProjectUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('code') is None:
                raise MissingParameters('code')
            if not Project.validate_project_code(request.data.get('code')):
                raise EntityError('code')
            
            project = self.usecase(code=request.data.get('code'), user_id=requester_user.user_id)
            viewmodel = DeleteProjectViewModel(project)
            
            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])