
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from .create_member_usecase import  CreateMemberUsecase
from .create_member_viewmodel import  CreateMemberViewmodel
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class CreateMemberController:
    
    def __init__(self, usecase: CreateMemberUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('name') is None:
                raise MissingParameters('name')
            if request.data.get('email_dev') is None:
                raise MissingParameters('email_dev')
            if request.data.get('email') is None:
                raise MissingParameters('email')
            if request.data.get('ra') is None:
                raise MissingParameters('ra')

            role = request.data.get('role')
            if role not in [role_value.value for role_value in ROLE]:
                raise EntityError('role')
            role = ROLE[role]
            if request.data.get('role') is None:
                raise MissingParameters('role')
            
            stack = request.data.get('stack')
            if stack not in [stack_value.value for stack_value in STACK]:
                raise EntityError('stack')
            stack = STACK[stack]
            if request.data.get('stack') is None:
                raise MissingParameters('stack')
            if request.data.get('year') is None:
                raise MissingParameters('year')
            if request.data.get('cellphone') is None:
                raise MissingParameters('cellphone')
            course = request.data.get('course')
            if course not in [course_value.value for course_value in COURSE]:
                raise EntityError('course')
            course = COURSE[course]
            if request.data.get('course') is None:
                raise MissingParameters('course')
            if request.data.get('hired_date') is None:
                raise MissingParameters('hired_date')
  

            # if request.data.get('stack_tags') is not None:
            #     if type(request.data.get('stack_tags')) is not list:
            #         raise EntityError('stack_tags')
            #     for value in request.data.get('stack_tags'):
            #         if value not in [stack.value for stack in STACK]:
            #             raise EntityError('stack_tags')
            #     stack_tags = [STACK[value] for value in request.data.get('stack_tags')]
            # else:
            #     stack_tags = None
                
            # if request.data.get('action_type_tag') is not None:
            #     action_type_tag_str = request.data.get('action_type_tag')

            #     if action_type_tag_str not in [action_type.value for action_type in ACTION_TYPE]:
            #         raise EntityError('action_type_tag')
                    
            #     action_type_tag = ACTION_TYPE[action_type_tag_str]
            # else:
            #     action_type_tag = None
                
            # if not Member.validate_ra(request.data.get('owner_ra')):
            #     raise EntityError('owner_ra')
            
            # if request.data.get('associated_members_ra') is not None:
            #     if type(request.data.get('associated_members_ra')) is not list:
            #         raise EntityError('associated_members_ra')
            #     for ra in request.data.get('associated_members_ra'):
            #         if not Member.validate_ra(ra):
            #             raise EntityError('associated_members_ra')

                   
            member = self.usecase(
                name=request.data.get('name'),
                email_dev=request.data.get('email_dev'),
                email=request.data.get('email'),
                ra=request.data.get('ra'),
                role=role,
                stack=stack,
                year=request.data.get('year'),
                cellphone=request.data.get('cellphone'),
                course=course,
                deactivated_date=request.data.get('deactivated_date')                            
            )
            
            viewmodel = CreateMemberViewmodel(member=member)
            
            return Created(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])