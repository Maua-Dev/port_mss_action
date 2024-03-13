from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from .create_action_usecase import CreateActionUsecase
from .create_action_viewmodel import CreateActionViewmodel
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class CreateActionController:
    
    def __init__(self, usecase: CreateActionUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('owner_ra') is None:
                raise MissingParameters('owner_ra')
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
            if request.data.get('associated_members_ra') is None:
                raise MissingParameters('associated_members_ra')
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')
            
           
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
                
            if not Member.validate_ra(request.data.get('owner_ra')):
                raise EntityError('owner_ra')
            
            if not Member.validate_user_id(request.data.get('user_id')):
                raise EntityError('user_id')
            
            if request.data.get('associated_members_ra') is not None:
                if type(request.data.get('associated_members_ra')) is not list:
                    raise EntityError('associated_members_ra')
                for ra in request.data.get('associated_members_ra'):
                    if not Member.validate_ra(ra):
                        raise EntityError('associated_members_ra')

                   
            action = self.usecase(
                owner_ra=request.data.get('owner_ra'),
                user_id=request.data.get('user_id'),
                start_date=request.data.get('start_date'),
                end_date=request.data.get('end_date'),
                duration=request.data.get('duration'),
                story_id=request.data.get('story_id'),
                title=request.data.get('title'),
                description=request.data.get('description'),
                associated_members_ra=request.data.get('associated_members_ra'),
                project_code=request.data.get('project_code'),
                stack_tags=stack_tags,
                action_type_tag=action_type_tag
            )
            
            viewmodel = CreateActionViewmodel(action=action)
            
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