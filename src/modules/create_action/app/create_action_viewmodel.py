from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE

from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    user_id: str
    start_date: int
    end_date: int
    duration: int
    action_id: str
    is_valid: bool
    story_id: int = None
    title: str
    description: str
    project_code: str
    associated_members_user_ids: List[str] = []
    stack_tags: List[STACK]
    action_type_tag: ACTION_TYPE
    
    def __init__(self, action: Action):
        self.user_id = action.user_id
        self.start_date = action.start_date
        self.end_date = action.end_date
        self.duration = action.duration
        self.action_id = action.action_id
        self.is_valid = action.is_valid
        self.story_id = action.story_id
        self.title = action.title
        self.description = action.description
        self.project_code = action.project_code
        self.associated_members_user_ids = action.associated_members_user_ids
        self.stack_tags = action.stack_tags
        self.action_type_tag = action.action_type_tag
        
    def to_dict(self):
        return {
            'user_id' : self.user_id,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'duration' : self.duration,
            'action_id' : self.action_id,
            'is_valid' : self.is_valid,
            'story_id' : self.story_id,
            'title' : self.title,
            'description' : self.description,
            'project_code' : self.project_code,
            'associated_members_user_ids' : self.associated_members_user_ids,
            'stack_tags' : [tag.value for tag in self.stack_tags],
            'action_type_tag' : self.action_type_tag.value
        }

class CreateActionViewmodel:
    action: Action
    
    def __init__(self, action: Action):
        self.action = action
    
    def to_dict(self) -> dict:
        return {
            'action' : ActionViewModel(self.action).to_dict(),
            'message' : 'the action was created'
        }