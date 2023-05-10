from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from .create_action_usecase import CreateActionUsecase
from .create_action_viewmodel import CreateActionViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse

class CreateActionController:
    repo = ActionRepositoryMock()
    
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
            if request.data.get('action_id') is None:
                raise MissingParameters('action_id')
            if request.data.get('title') is None:
                raise MissingParameters('title')
            if request.data.get('project_code') is None:
                raise MissingParameters('project_code')
            
            if request.data.get('stack_tags') is not None:
                if type(request.data.get('stack_tags')) is not list:
                    raise EntityError('stack_tags')
                for value in request.data.get('stack_tags'):
                    if value not in [stack.value for stack in STACK]:
                        raise EntityError('stack_tags')
                stack_tags = [STACK[value] for value in request.data.get('stack_tags')]
            else:
                stack_tags = None
                
            if request.data.get('action_type_tags') is not None:
                if type(request.data.get('action_type_tags')) is not list:
                    raise EntityError('action_type_tags')
                for value in request.data.get('action_type_tags'):
                    if value not in [action_type.value for action_type in ACTION_TYPE]:
                        raise EntityError('action_type_tags')
                action_type_tags = [ACTION_TYPE[value] for value in request.data.get('action_type_tags')]
            else:
                action_type_tags = None
            
            action = Action(
                owner_ra=request.data.get('owner_ra'),
                start_date=request.data.get('start_date'),
                end_date=request.data.get('end_date'),
                duration=request.data.get('duration'),
                action_id=request.data.get('action_id'),
                title=request.data.get('title'),
                associated_members_ra=request.data.get('associated_members_ra'),
                project_code=request.data.get('project_code'),
                stack_tags=stack_tags,
                action_type_tags=action_type_tags
            )
            
            viewmodel = CreateActionViewmodel(action=self.usecase(action=action))
            
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