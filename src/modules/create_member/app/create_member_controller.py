
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .create_member_usecase import  CreateMemberUsecase
from .create_member_viewmodel import  CreateMemberViewmodel
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class CreateMemberController:
    
    def __init__(self, usecase: CreateMemberUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
            if request.data.get('ra') is None:
                raise MissingParameters('ra')
            if type(request.data.get('ra')) is not str:
                raise WrongTypeParameter(fieldName='ra', fieldTypeExpected='str', fieldTypeReceived=type( request.data.get('ra') ))
           


            
            if not Member.validate_email_dev(request.data.get('email_dev')):
                raise EntityError('email_dev')   
            if request.data.get('email_dev') is None:
                raise MissingParameters('email_dev')
          

            
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
            
            if not Member.validate_year(request.data.get('year') ):
                 raise EntityError("year")
            if request.data.get('year') is None:
                raise MissingParameters('year')

            if not Member.validate_cellphone(request.data.get('cellphone')):
                raise EntityError("cellphone")            
            if request.data.get('cellphone') is None:
                raise MissingParameters('cellphone')
            
            course = request.data.get('course')
            if course not in [course_value.value for course_value in COURSE]:
                raise EntityError('course')
            course = COURSE[course]
            if request.data.get('course') is None:
                raise MissingParameters('course')
            
            if not Member.validate_photo(request.data.get('photo')):
                raise EntityError('photo')
            
            

            
            
            member = self.usecase(
                name=str(requester_user.name),
                email_dev=request.data.get('email_dev'),
                email=str(requester_user.email),
                ra=request.data.get('ra'),
                role=role,
                stack=stack,
                year=request.data.get('year'),
                cellphone=request.data.get('cellphone'),
                course=course,
                user_id=str(requester_user.user_id),
                photo = request.data.get('photo')
                                          
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