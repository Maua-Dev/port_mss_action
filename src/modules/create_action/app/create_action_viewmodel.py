from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE

from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    owner_ra: str
    start_date: int
    end_date: int
    duration: int
    action_id: str
    story_id: int = None
    title: str
    project_code: str
    associated_members_ra: List[str] = None
    stack_tags: List[STACK]
    action_type_tag: ACTION_TYPE
    
    def __init__(self, action: Action):
        self.owner_ra = action.owner_ra
        self.start_date = action.start_date
        self.end_date = action.end_date
        self.duration = action.duration
        self.action_id = action.action_id
        self.story_id = action.story_id
        self.title = action.title
        self.project_code = action.project_code
        self.associated_members_ra = action.associated_members_ra
        self.stack_tags = action.stack_tags
        self.action_type_tag = action.action_type_tag
        
    def to_dict(self):
        return {
            'owner_ra' : self.owner_ra,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'duration' : self.duration,
            'action_id' : self.action_id,
            'story_id' : self.story_id,
            'title' : self.title,
            'project_code' : self.project_code,
            'associated_members_ra' : self.associated_members_ra,
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