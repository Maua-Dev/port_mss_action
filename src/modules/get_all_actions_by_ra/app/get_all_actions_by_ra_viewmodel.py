from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    start_date: int
    end_date: int
    duration: int
    action_id: str
    title: str
    project_code: str
    stack_tags: List[STACK] = None
    action_type_tags: List[ACTION_TYPE] = None
    is_owner : bool
    
    def __init__(self, associated_action: AssociatedAction):
        self.start_date = associated_action.action.start_date
        self.end_date = associated_action.action.end_date
        self.duration = self.end_date - self.start_date
        self.action_id = associated_action.action.action_id
        self.title = associated_action.action.title
        self.project_code = associated_action.action.project_code
        self.stack_tags = associated_action.action.stack_tags
        self.action_type_tags = associated_action.action.action_type_tags
        self.is_owner = associated_action.action.owner_ra == associated_action.member_ra
        
    def to_dict(self):
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "duration": self.duration,
            "action_id": self.action_id,
            "title": self.title,
            "project_code": self.project_code,
            "stack_tags": [tag.value for tag in self.stack_tags],
            "action_type_tags": [tag.value for tag in self.action_type_tags],
            "is_owner": self.is_owner,
        }
        

class GetAllActionsByRaViewmodel:
    associated_actions: List[AssociatedAction]
    ra: str
    
    def __init__(self, associated_actions: List[AssociatedAction], ra: str):
        self.associated_actions = associated_actions
        self.ra = ra
    
    def to_dict(self):
        return {
            "actions": [ActionViewModel(action).to_dict() for action in self.associated_actions],
            "ra": self.ra,
            "message": "the actions were retrieved"
        }