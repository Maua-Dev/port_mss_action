from .update_action_usecase import UpdateActionUsecase
from .update_action_viewmodel import UpdateActionViewmodel
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.domain.enums.stack_enum import STACK


class UpdateActionController:
    
    def __init__(self, usecase: UpdateActionUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            action_id = request.data.get('action_id')
            if action_id is None:
                raise MissingParameters('action_id')
            if type(action_id) is not str:
                raise WrongTypeParameter(fieldName='action_id', fieldTypeExpected='str', fieldTypeReceived=type(action_id))
            if not Action.validate_action_id(action_id):
                raise EntityError('action_id')

            new_user_id = request.data.get('new_user_id')
            if new_user_id is not None:
                if type(new_user_id) is not str:
                    raise WrongTypeParameter(fieldName='new_user_id', fieldTypeExpected='str', fieldTypeReceived=type(new_user_id))
                if not Member.validate_user_id(new_user_id):
                    raise EntityError('new_user_id')
            
            new_start_date = request.data.get('new_start_date')
            if new_start_date is not None:
                if type(new_start_date) is not int:
                    raise WrongTypeParameter(fieldName='new_start_date', fieldTypeExpected='int', fieldTypeReceived=type(new_start_date))
                if not 1000000000000 < new_start_date < 10000000000000:
                    raise EntityError('new_start_date')

            new_end_date = request.data.get('new_end_date')
            if new_end_date is not None:
                if type(new_end_date) is not int:
                    raise WrongTypeParameter(fieldName='new_end_date', fieldTypeExpected='int', fieldTypeReceived=type(new_end_date))
                if not 1000000000000 < new_end_date < 10000000000000:
                    raise EntityError('new_end_date')
            
            if new_start_date and new_end_date and new_start_date > new_end_date:
                raise EntityError('new_start_date and new_end_date')
            
            new_duration = request.data.get('new_duration')
            if new_duration is not None:
                if type(new_duration) is not int:
                    raise WrongTypeParameter(fieldName='new_duration', fieldTypeExpected='int', fieldTypeReceived=type(new_duration))
                if new_duration < 0:
                    raise EntityError('new_duration')
                
            if new_start_date and new_end_date and new_duration:
                if not Action.validate_duration(duration=new_duration, start_date=new_start_date, end_date=new_end_date):
                    raise EntityError('new_duration')
            
            new_story_id = -1
            if 'new_story_id' in request.data.keys():
                new_story_id = request.data.get('new_story_id')
                if new_story_id is not None:
                    if type(new_story_id) is not int:
                        raise WrongTypeParameter(fieldName='new_story_id', fieldTypeExpected='int', fieldTypeReceived=type(new_story_id))
                    if not Action.validate_story_id(new_story_id):
                        raise EntityError('new_story_id')
                
            new_title = request.data.get('new_title')
            if new_title is not None:
                if type(new_title) is not str:
                    raise WrongTypeParameter(fieldName='new_title', fieldTypeExpected='str', fieldTypeReceived=type(new_title))
                if not Action.validate_title(new_title):
                    raise EntityError('new_title')
                
            new_description = ''
            if 'new_description' in request.data.keys():
                new_description = request.data.get('new_description')
                if new_description is not None:
                    if type(new_description) is not str:
                        raise WrongTypeParameter(fieldName='new_description', fieldTypeExpected='str', fieldTypeReceived=type(new_description))
                    if not Action.validate_description(new_description):
                        raise EntityError('new_description')
                
            new_project_code = request.data.get('new_project_code')
            if new_project_code is not None:
                if type(new_project_code) is not str:
                    raise WrongTypeParameter(fieldName='new_project_code', fieldTypeExpected='str', fieldTypeReceived=type(new_project_code))
                if not Action.validate_project_code(new_project_code):
                    raise EntityError('new_project_code')
                
            new_associated_members_user_ids = request.data.get('new_associated_members_user_ids')
            if new_associated_members_user_ids is not None:
                if type(new_associated_members_user_ids) is not list:
                    raise WrongTypeParameter(fieldName='new_associated_members_user_ids', fieldTypeExpected='list', fieldTypeReceived=type(new_associated_members_user_ids))
                for user_id in new_associated_members_user_ids:
                    if type(user_id) is not str:
                        raise WrongTypeParameter(fieldName='new_associated_members_user_ids', fieldTypeExpected='str', fieldTypeReceived=type(user_id))
                    if not Member.validate_user_id(user_id):
                        raise EntityError('new_associated_members_user_ids')
                
            new_stack_tags = request.data.get('new_stack_tags')
            if new_stack_tags is not None:
                if type(new_stack_tags) is not list:
                    raise WrongTypeParameter(fieldName='new_stack_tags', fieldTypeExpected='list', fieldTypeReceived=type(new_stack_tags))
                for value in new_stack_tags:
                    if type(value) is not str:
                        raise WrongTypeParameter(fieldName='new_stack_tags', fieldTypeExpected='str', fieldTypeReceived=type(value))
                    if value not in [stack.value for stack in STACK]:
                        raise EntityError('new_stack_tags')
                new_stack_tags = [STACK(value) for value in new_stack_tags]
                
            new_action_type_tag = request.data.get('new_action_type_tag')
            if new_action_type_tag is not None:
                if type(new_action_type_tag) is not str:
                    raise WrongTypeParameter(fieldName='new_action_type_tag', fieldTypeExpected='str', fieldTypeReceived=type(new_action_type_tag))
                if new_action_type_tag not in [action_type.value for action_type in ACTION_TYPE]:
                    raise EntityError('new_action_type_tag')
                new_action_type_tag = ACTION_TYPE(new_action_type_tag)

            new_is_valid = request.data.get('new_is_valid')
            if request.data.get('new_is_valid') is not None:
                if type(new_is_valid) is not bool:
                    raise WrongTypeParameter(fieldName='new_is_valid', fieldTypeExpected='bool', fieldTypeReceived=type(new_is_valid))

            
            action = self.usecase(
                action_id=action_id,
                new_user_id=new_user_id,
                new_start_date=new_start_date,
                new_end_date=new_end_date,
                new_duration=new_duration,
                new_story_id=new_story_id,
                new_title=new_title,
                new_description=new_description,
                new_project_code=new_project_code,
                new_associated_members_user_ids=new_associated_members_user_ids,
                new_stack_tags=new_stack_tags,
                new_action_type_tag=new_action_type_tag,
                new_is_valid=new_is_valid
            )
            
            viewmodel = UpdateActionViewmodel(action=action)    

            return OK(viewmodel.to_dict())

            
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])