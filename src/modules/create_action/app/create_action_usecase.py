from typing import List, Optional
import uuid
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound

class CreateActionUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, owner_ra: str, user_id: str, is_valid: bool, start_date: int, stack_tags: List[STACK], end_date: int, duration: int, title: str, project_code: str, action_type_tag: ACTION_TYPE, associated_members_user_ids: List[str] = [], description: Optional[str] = None, story_id: Optional[int] = None) -> Action:
        
        action_id = str(uuid.uuid4())
        
        for ra in [user_id] + associated_members_user_ids:
            if not self.repo.get_member(user_id):
                raise NoItemsFound(ra)
        
        action = Action(owner_ra, user_id, start_date, stack_tags, end_date, duration, action_id, is_valid, title, project_code, action_type_tag, associated_members_user_ids, description, story_id)        
        
        self.repo.create_action(action)
        self.repo.create_associated_action(AssociatedAction(owner_ra, action_id, start_date, user_id))
        if action.associated_members_user_ids:
            for ra in action.associated_members_user_ids:
                associated_action = AssociatedAction(ra, action_id, start_date)
                self.repo.create_associated_action(associated_action)
        
        return action