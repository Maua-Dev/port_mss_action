from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE

from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    owner_ra: str
    start_time: int
    end_time: int
    duration: int
    action_id: str
    title: str
    project_code: str
    associated_members_ra: List[str] = None
    stack_tags: List[STACK] = None
    action_type_tags: List[ACTION_TYPE] = None
    
    def __init__(self, action: Action):
        self.owner_ra = action.owner_ra
        self.start_time = action.start_time
        self.end_time = action.end_time
        self.duration = self.end_time - self.start_time
        self.action_id = action.action_id
        self.title = action.title
        self.project_code = action.project_code
        self.associated_members_ra = action.associated_members_ra
        self.stack_tags = action.stack_tags
        self.action_type_tags = action.action_type_tags
        
    def to_dict(self):
        return {
            'owner_ra' : self.owner_ra,
            'start_time' : self.start_time,
            'end_time' : self.end_time,
            'duration' : self.duration,
            'action_id' : self.action_id,
            'title' : self.title,
            'project_code' : self.project_code,
            'associated_members_ra' : self.associated_members_ra,
            'stack_tags' : [tag.value for tag in self.stack_tags],
            'action_type_tags' : [tag.value for tag in self.action_type_tags]
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