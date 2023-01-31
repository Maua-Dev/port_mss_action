import datetime
from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    ra: str
    date: int
    action_id: str
    title: str
    duration: datetime.time
    project_code: str
    stack_tags: List[STACK] = None
    action_type_tags: List[ACTION_TYPE] = None
    is_owner : bool
    
    def __init__(self, action: Action, ra: str):
        self.ra = ra
        self.date = action.date
        self.action_id = action.action_id
        self.title = action.title
        self.duration = action.duration
        self.project_code = action.project_code
        self.stack_tags = action.stack_tags
        self.action_type_tags = action.action_type_tags
        self.is_owner = action.owner_ra == ra
        
    def to_dict(self):
        return {
            "ra": self.ra,
            "date": self.date,
            "action_id": self.action_id,
            "title": self.title,
            "duration": self.duration.strftime("%H:%M:%S"),
            "project_code": self.project_code,
            "stack_tags": [tag.value for tag in self.stack_tags],
            "action_type_tags": [tag.value for tag in self.action_type_tags],
            "is_owner": self.is_owner,
        }
        

class GetAllActionsByRaViewmodel:
    actions: List[Action]
    ra: str
    
    def __init__(self, actions: List[Action], ra: str):
        self.actions = actions
        self.ra = ra
    
    def to_dict(self):
        return {
            "actions": [ActionViewModel(action, ra=self.ra).to_dict() for action in self.actions],
            "message": "the actions were retrieved"
        }