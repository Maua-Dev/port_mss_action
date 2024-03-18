from typing import List, Optional, Tuple
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    start_date: int
    end_date: int
    duration: int
    action_id: str
    story_id: int = None
    title: str
    description: str
    project_code: str
    associated_members_ra: List[str] = []
    stack_tags: List[STACK]
    action_type_tag: ACTION_TYPE
    
    def __init__(self, action: Action):
        self.start_date = action.start_date
        self.end_date = action.end_date
        self.duration = action.duration
        self.action_id = action.action_id
        self.story_id = action.story_id
        self.title = action.title
        self.description = action.description
        self.project_code = action.project_code
        self.associated_members_user_ids = action.associated_members_user_ids
        self.stack_tags = action.stack_tags
        self.action_type_tag = action.action_type_tag
        
    def to_dict(self):
        return {
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'duration' : self.duration,
            'action_id' : self.action_id,
            'story_id' : self.story_id,
            'title' : self.title,
            'description' : self.description,
            'project_code' : self.project_code,
            'associated_members_user_ids' : self.associated_members_user_ids,
            'stack_tags' : [tag.value for tag in self.stack_tags],
            'action_type_tag' : self.action_type_tag.value
        }

class GetHistoryViewmodel:
    actions: List[ActionViewModel]
    last_evaluated_key: Optional[Tuple[str, int]] = None
    
    def __init__(self, actions: List[Action], last_evaluated_key: Optional[Tuple[str, int]] = None):
        self.actions = [ActionViewModel(action) for action in actions]
        self.last_evaluated_key = last_evaluated_key
        
    def to_dict(self) -> dict:
        return {
            'actions' : [action.to_dict() for action in self.actions],
            'last_evaluated_key' : {'action_id' : self.last_evaluated_key[0], 'start_date' : self.last_evaluated_key[1]} if self.last_evaluated_key else None,
            'message' : 'the history was retrieved'
        }