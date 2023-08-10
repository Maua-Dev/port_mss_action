from typing import List, Optional
from src.shared.domain.entities.action import Action
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateActionUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, action_id: str,
                new_owner_ra: Optional[str] = None, 
                new_start_date: Optional[int] = None, 
                new_end_date: Optional[int] = None, 
                new_duration: Optional[int] = None, 
                new_story_id: Optional[str] = None, 
                new_title: Optional[str] = None, 
                new_description: Optional[str] = None, 
                new_project_code: Optional[str] = None, 
                new_associated_members_ra: Optional[List[str]] = None, 
                new_stack_tags: Optional[List[str]] = None, 
                new_action_type_tag: Optional[str] = None) -> Action:
        
        action = self.repo.get_action(action_id)
        if not action:
            raise NoItemsFound('action')
        
        members = ['No members']
        start_date = new_start_date if new_start_date is not None else action.start_date
        if new_associated_members_ra and new_owner_ra:
            members = [new_owner_ra] + new_associated_members_ra
        elif new_associated_members_ra:
            members = new_associated_members_ra + [action.owner_ra]
        elif new_owner_ra:
            members = [new_owner_ra] + action.associated_members_ra
        else:
            members = action.associated_members_ra + [action.owner_ra]
        if members != ['No members'] and set(members) != set([action.owner_ra] + action.associated_members_ra):
            self.repo.batch_update_associated_action_members(action_id, members, start_date=start_date)
        elif start_date != action.start_date:
            self.repo.batch_update_associated_action_members(action_id, members, start_date=new_start_date)
        
        return self.repo.update_action(action_id, new_owner_ra, new_start_date, new_end_date, new_duration, new_story_id, new_title, new_description, new_project_code, new_associated_members_ra, new_stack_tags, new_action_type_tag)