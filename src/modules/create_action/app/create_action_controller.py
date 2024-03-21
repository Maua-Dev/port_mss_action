from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound, UnregisteredUser
from .create_action_usecase import CreateActionUsecase
from .create_action_viewmodel import CreateActionViewmodel
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

class CreateActionController:
    
    def __init__(self, usecase: CreateActionUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('start_date') is None:
                raise MissingParameters('start_date')
            if request.data.get('end_date') is None:
                raise MissingParameters('end_date')
            if request.data.get('duration') is None:
                raise MissingParameters('duration')
            if request.data.get('title') is None:
                raise MissingParameters('title')
            if request.data.get('project_code') is None:
                raise MissingParameters('project_code')
            if request.data.get('associated_members_user_ids') is None:
                raise MissingParameters('associated_members_user_ids')
            if request.data.get('is_valid') is None:
                raise MissingParameters('is_valid')
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if type(requester_user.user_id) is not str:
                raise WrongTypeParameter(fieldName='user_id', fieldTypeExpected='str', fieldTypeReceived=type(requester_user.user_id))
            if not Member.validate_user_id(requester_user.user_id):
                raise EntityError('user_id')
           
            if request.data.get('story_id') is not None:
                if type(request.data.get('story_id')) is not int:
                    raise EntityError('story_id')
                story_id = request.data.get('story_id')
            else:
                story_id = None
                

            if request.data.get('stack_tags') is not None:
                if type(request.data.get('stack_tags')) is not list:
                    raise EntityError('stack_tags')
                for value in request.data.get('stack_tags'):
                    if value not in [stack.value for stack in STACK]:
                        raise EntityError('stack_tags')
                stack_tags = [STACK[value] for value in request.data.get('stack_tags')]
            else:
                stack_tags = None
                
            if request.data.get('action_type_tag') is not None:
                action_type_tag_str = request.data.get('action_type_tag')

                if action_type_tag_str not in [action_type.value for action_type in ACTION_TYPE]:
                    raise EntityError('action_type_tag')
                    
                action_type_tag = ACTION_TYPE[action_type_tag_str]
            else:
                action_type_tag = None
            
            if request.data.get('associated_members_user_ids') is not None:
                if type(request.data.get('associated_members_user_ids')) is not list:
                    raise EntityError('associated_members_user_ids')
                for user_id in request.data.get('associated_members_user_ids'):
                    if not Member.validate_user_id(user_id):
                        raise EntityError('associated_members_user_ids')

                   
            action = self.usecase(
                user_id=requester_user.user_id,
                start_date=request.data.get('start_date'),
                end_date=request.data.get('end_date'),
                duration=request.data.get('duration'),
                is_valid=request.data.get('is_valid'),
                story_id=request.data.get('story_id'),
                title=request.data.get('title'),
                description=request.data.get('description'),
                associated_members_user_ids=request.data.get('associated_members_user_ids'),
                project_code=request.data.get('project_code'),
                stack_tags=stack_tags,
                action_type_tag=action_type_tag
            )
            
            viewmodel = CreateActionViewmodel(action=action)
            
            return Created(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except UnregisteredUser as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])