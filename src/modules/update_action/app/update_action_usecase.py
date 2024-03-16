from typing import List, Optional
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateActionUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, action_id: str,
                new_user_id: Optional[str] = None, 
                new_start_date: Optional[int] = None, 
                new_end_date: Optional[int] = None, 
                new_duration: Optional[int] = None, 
                new_story_id: Optional[str] = -1, 
                new_title: Optional[str] = None, 
                new_description: Optional[str] = '', 
                new_project_code: Optional[str] = None, 
                new_associated_members_user_ids: Optional[List[str]] = None, 
                new_stack_tags: Optional[List[STACK]] = None, 
                new_action_type_tag: Optional[ACTION_TYPE] = None,
                new_is_valid: Optional[bool] = None) -> Action:
        
        action = self.repo.get_action(action_id)
        if not action:
            raise NoItemsFound('action')
        
        
        members = None
        start_date = new_start_date if new_start_date is not None else action.start_date
        if new_associated_members_user_ids and new_user_id:
            members = [new_user_id] + new_associated_members_user_ids
        elif new_associated_members_user_ids:
            members = new_associated_members_user_ids + [action.user_id]
        elif new_user_id:
            members = [new_user_id] + action.associated_members_user_ids
        else:
            members = action.associated_members_user_ids + [action.user_id]
        if members != None and set(members) != set([action.user_id] + action.associated_members_user_ids):
            self.repo.batch_update_associated_action_members(action_id, members, start_date=start_date)
        elif start_date != action.start_date:
            self.repo.batch_update_associated_action_members(action_id, members, start_date=new_start_date)
            
        description = new_description if new_description is not '' else action.description
        story_id = new_story_id if new_story_id is not -1 else action.story_id
        return self.repo.update_action(action_id, new_user_id, new_start_date, new_end_date, new_duration, story_id, new_title, description, new_project_code, new_associated_members_user_ids, new_stack_tags, new_action_type_tag, new_is_valid)