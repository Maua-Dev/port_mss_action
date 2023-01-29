import datetime
from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK

class ActionViewModel:
    owner_ra: str
    date: datetime.datetime
    action_id: str
    title: str
    duration: datetime.time
    project_code: str
    associated_members_ra: List[str] = None
    stack_tags: List[STACK] = None
    action_type_tags: List[ACTION_TYPE] = None
    
    def __init__(self, action: Action):
        self.owner_ra = action.owner_ra
        self.date = action.date
        self.action_id = action.action_id
        self.title = action.title
        self.duration = action.duration
        self.project_code = action.project_code
        self.associated_members_ra = action.associated_members_ra
        self.stack_tags = action.stack_tags
        self.action_type_tags = action.action_type_tags
        
    def to_dict(self):
        return {
            "owner_ra": self.owner_ra,
            "date": self.date.isoformat(),
            "action_id": self.action_id,
            "title": self.title,
            "duration": self.duration.strftime("%H:%M:%S"),
            "project_code": self.project_code,
            "associated_members_ra": [ra for ra in self.associated_members_ra],
            "stack_tags": [tag.value for tag in self.stack_tags],
            "action_type_tags": [tag.value for tag in self.action_type_tags]
        }
        

class GetAllActionsByRaViewmodel:
    actions: List[Action]
    
    def __init__(self, actions: List[Action]):
        self.actions = actions
    
    def to_dict(self):
        return {
            "actions": [ActionViewModel(action).to_dict() for action in self.actions],
            "message": "the actions were retrieved"
        }