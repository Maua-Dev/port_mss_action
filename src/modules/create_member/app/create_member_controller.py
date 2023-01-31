import datetime
from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.modules.create_member.app.create_member_viewmodel import CreateMemberViewmodel
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, Forbidden, InternalServerError, NotFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class CreateMemberController:
    repo = ActionRepositoryMock()
    def __init__(self, usecase: CreateMemberUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('name') is None:
                raise MissingParameters('name')
            if request.data.get('email') is None:
                raise MissingParameters('email')
            if request.data.get('ra') is None:
                raise MissingParameters('ra')
            if request.data.get('role') is None:
                raise MissingParameters('role')
            if request.data.get('stack') is None:
                raise MissingParameters('stack')
            if request.data.get('year') is None:
                raise MissingParameters('year')
            if request.data.get('cellphone') is None:
                raise MissingParameters('cellphone')
            if request.data.get('course') is None:
                raise MissingParameters('course')
            if request.data.get('hired_date') is None:
                raise MissingParameters('hired_date')
            if request.data.get('active') is None:
                raise MissingParameters('active')
            if request.data.get('projects') is None:
                raise MissingParameters('projects')

            if request.data.get('role') not in [role.value for role in ROLE]:
                raise EntityError('role')

            if request.data.get('stack') not in [stack.value for stack in STACK]:
                raise EntityError('stack')
            
            if request.data.get('course') not in [course.value for course in COURSE]:
                raise EntityError('course')
            
            if request.data.get('active') not in [active.value for active in ACTIVE]:
                raise EntityError('active')
            
            if type(request.data.get('projects')) is not list:
                raise EntityError('projects')
            
            try:
                projects = [Project(**project) for project in request.data.get('projects')]
            except:
                raise EntityError('projects')
            
            try:
                hired_date = datetime.datetime.strptime(request.data.get('hired_date'), '%Y-%m-%dT%H:%M:%S')
            except:
                raise EntityError('hired_date')
            
            try:
                deactivated_date = None if request.data.get('deactivated_date') is None else datetime.datetime.strptime(request.data.get('deactivated_date'), '%Y-%m-%dT%H:%M:%S')
            except:
                raise EntityError('deactivated_date')
            
            member = self.usecase(
                name=request.data.get('name'),
                email=request.data.get('email'),
                ra=request.data.get('ra'),
                role=ROLE[request.data.get('role')],
                stack=STACK[request.data.get('stack')],
                year=request.data.get('year'),
                cellphone=request.data.get('cellphone'),
                course=COURSE[request.data.get('course')],
                hired_date=hired_date,
                deactivated_date=deactivated_date,
                active=ACTIVE[request.data.get('active')],
                projects=projects
            )
            
            viewmodel = CreateMemberViewmodel(member=member)
            
            return Created(viewmodel.to_dict())
        
        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except DuplicatedItem as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])