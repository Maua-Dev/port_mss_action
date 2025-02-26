

from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound 
from .download_projects_usecase import DownloadProjectsUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, OK, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeFile, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE

from src.shared.domain.enums.stack_enum import STACK
class DownloadProjectsController:
    def __init__(self, usecase: DownloadProjectsUsecase):
        self.usecase = usecase
     
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            
            if request.data.get('project_code') is None:
                raise MissingParameters('project_code')
            
            project_code = request.data.get('project_code')
            start = request.data.get('start')
            end = request.data.get('end')
            if request.data.get('member_user_id') is None:
                raise MissingParameters('member_user_id')
            member_user_id = request.data.get('member_user_id')
            if start is not None and type(start) != int:
                raise WrongTypeParameter('start')
            if end is not None and type(end) != int:    
                raise WrongTypeParameter('end')
            if member_user_id is not None and type(member_user_id) != str:  
                raise WrongTypeParameter('member_user_id')  
            if type(project_code) != str:
                raise WrongTypeParameter('project_code')
            if not Member.validate_user_id(member_user_id):
                raise EntityError('member_user_id')
            if not Member.validate_user_id(requester_user.user_id):
                raise EntityError('requester_user')

     
            usecase = self.usecase(
                user_id=str(requester_user.user_id),
                start=start,
                end=end,
                project_code=project_code,
                member_user_id=member_user_id,
            )

            message = {"Link": usecase}
            response = OK(message)

            return response
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except WrongTypeFile as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])