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
        
    def __call__(self, owner_ra: str, start_date: int, stack_tags: List[STACK], end_date: int, duration: int, title: str, project_code: str, action_type_tag: ACTION_TYPE, associated_members_ra: List[str] = [], description: Optional[str] = None, story_id: Optional[int] = None) -> Action:
        
        action_id = str(uuid.uuid4())
        
        action = Action(owner_ra, start_date, stack_tags, end_date, duration, action_id, title, project_code, action_type_tag, associated_members_ra, description, story_id)        
        
        self.repo.create_action(action)
        self.repo.create_associated_action(AssociatedAction(owner_ra, action))
        if action.associated_members_ra:
            for ra in action.associated_members_ra:
                associated_action = AssociatedAction(ra, action)
                self.repo.create_associated_action(associated_action)
        
        return action