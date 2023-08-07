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
        
        if set([new_owner_ra] + new_associated_members_ra) != set([action.owner_ra] + action.associated_members_ra):
            self.repo.batch_update_associated_action_members(action_id, [new_owner_ra] + new_associated_members_ra, start_date=new_start_date)
        elif new_start_date != action.start_date:
            self.repo.batch_update_associated_action_start(action_id, new_start_date)
        
        return self.repo.update_action(action_id, new_owner_ra, new_start_date, new_end_date, new_duration, new_story_id, new_title, new_description, new_project_code, new_associated_members_ra, new_stack_tags, new_action_type_tag)