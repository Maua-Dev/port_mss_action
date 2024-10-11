from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from .update_member_usecase import UpdateMemberUsecase
from .update_member_viewmodel import UpdateMemberViewmodel
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserNotAllowed
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError, NotFound
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK

class UpdateMemberController:
    
    def __init__(self, usecase: UpdateMemberUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            repo = MemberRepositoryMock()
            member = repo.get_member(user_id=requester_user.user_id)

            new_name = request.data.get('new_name')
            if new_name is not None:
                if type(new_name) is not str:
                    raise WrongTypeParameter(fieldName='new_name', fieldTypeExpected='str', fieldTypeReceived=type(new_name))

            
            new_email_dev = request.data.get('new_email_dev')
            if new_email_dev is not None:
                if type(new_email_dev) is not str:
                    raise WrongTypeParameter(fieldName='new_email_dev', fieldTypeExpected='str', fieldTypeReceived=type(new_email_dev))
                if not Member.validate_email_dev(new_email_dev):
                    raise EntityError('new_email_dev')

            new_role = request.data.get('new_role')
            if new_role is not None:
                if type(new_role) is not str:
                    raise WrongTypeParameter(fieldName='new_role', fieldTypeExpected='ROLE', fieldTypeReceived=type(new_role))
                if new_role not in [role_value.value for role_value in ROLE]:
                    raise EntityError('new_role')
                new_role = ROLE[new_role]


            new_stack = request.data.get('new_stack')
            if new_stack is not None:
                if type(new_stack) is not str:
                    raise WrongTypeParameter(fieldName='new_stack', fieldTypeExpected='STACK', fieldTypeReceived=type(new_stack))
                if new_stack not in [stack_value.value for stack_value in STACK]:
                    raise EntityError('new_stack')
                new_stack = STACK[new_stack]
            
            new_year = request.data.get('new_year')
            if new_year is not None:
                if type(new_year) is not int:
                    raise WrongTypeParameter(fieldName='new_year', fieldTypeExpected='int', fieldTypeReceived=type(new_year))
                if new_year < 0 or new_year>6:
                    raise EntityError('new_year')
                
            new_cellphone = request.data.get('new_cellphone')
            if new_cellphone is not None:
                if type(new_cellphone) is not str:
                    raise WrongTypeParameter(fieldName='new_cellphone', fieldTypeExpected='str', fieldTypeReceived=type(new_cellphone))
                if not Member.validate_cellphone(new_cellphone):
                    raise EntityError('new_cellphone')

            new_course = request.data.get('new_course')
            if new_course is not None:
                if type(new_course) is not str:
                    raise WrongTypeParameter(fieldName='new_course', fieldTypeExpected='COURSE', fieldTypeReceived=type(new_course))
                if new_course not in [course_value.value for course_value in COURSE]:
                    raise EntityError('new_course')
                new_course = COURSE[new_course]

                            
            new_active = request.data.get('new_active')
            if new_active is not None:
                if type(new_active) is not str:
                    raise WrongTypeParameter(fieldName='new_active', fieldTypeExpected='ACTIVE', fieldTypeReceived=type(new_active))
                if new_active not in [active_value.value for active_value in ACTIVE]:
                    raise EntityError('new_active')
                new_active = ACTIVE[new_active]
            
            new_member_user_id = request.data.get('new_member_user_id')
            if new_member_user_id is not None:
                if type(new_member_user_id) is not str:
                    raise WrongTypeParameter(fieldName='new_member_user_id', fieldTypeExpected='str', fieldTypeReceived=type(new_member_user_id))
                          
            new_photo = request.data.get('new_photo')
            if new_photo is not None:
                if type(new_photo) is not str:
                    raise WrongTypeParameter(fieldName='new_photo', fieldTypeExpected='str', fieldTypeReceived=type(new_photo))
                if not Member.validate_photo(new_photo):
                    raise EntityError('new_photo')
                
            member = self.usecase(
                user_id=requester_user.user_id,
                new_name=new_name,
                new_email_dev=new_email_dev,
                new_role=new_role,
                new_stack=new_stack,
                new_year=new_year,
                new_cellphone=new_cellphone,
                new_course =new_course ,
                new_active=new_active,
                new_member_user_id=new_member_user_id,
                new_photo=new_photo
            )
            
            viewmodel = UpdateMemberViewmodel(member=member)    

            return OK(viewmodel.to_dict())

            
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except UserNotAllowed as err:
            return Forbidden(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])