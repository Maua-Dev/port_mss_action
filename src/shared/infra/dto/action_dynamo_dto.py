from decimal import Decimal
from typing import List, Optional
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE

from src.shared.domain.enums.stack_enum import STACK


class ActionDynamoDTO:
    owner_ra: str
    start_date: int
    end_date: int
    duration: int
    action_id: str
    is_valid: bool
    story_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    project_code: str
    associated_members_ra: List[str]
    stack_tags: List[STACK]
    action_type_tag: ACTION_TYPE
    
    def __init__(self, owner_ra: str, start_date: int, stack_tags: List[STACK], end_date: int, duration: int, action_id: str, is_valid: bool, title: str, project_code: str, action_type_tag: ACTION_TYPE, associated_members_ra: List[str] = [], description: Optional[str] = None, story_id: Optional[int] = None):
        self.owner_ra = owner_ra
        self.start_date = start_date
        self.stack_tags = stack_tags
        self.end_date = end_date
        self.duration = duration
        self.action_id = action_id
        self.is_valid = is_valid
        self.story_id = story_id
        self.title = title
        self.description = description
        self.project_code = project_code
        self.associated_members_ra = associated_members_ra
        self.action_type_tag = action_type_tag
        
    @staticmethod
    def from_entity(action: Action) -> "ActionDynamoDTO":
        return ActionDynamoDTO(
            owner_ra=action.owner_ra,
            start_date=action.start_date,
            stack_tags=action.stack_tags,
            end_date=action.end_date,
            duration=action.duration,
            action_id=action.action_id,
            is_valid=action.is_valid,
            story_id=action.story_id,
            title=action.title,
            description=action.description,
            project_code=action.project_code,
            associated_members_ra=action.associated_members_ra,
            action_type_tag=action.action_type_tag
        )
        
    def to_dynamo(self) -> dict: 
        data = {
            "entity": "action",
            "owner_ra": self.owner_ra,
            "stack_tags": [tag.value for tag in self.stack_tags],
            "start_date": Decimal(str(self.start_date)),
            "end_date": Decimal(str(self.end_date)),
            "duration": Decimal(str(self.duration)),
            "action_id": self.action_id,
            "is_valid": self.is_valid,
            "title": self.title,
            "project_code": self.project_code,
            "action_type_tag": self.action_type_tag.value,
            "associated_members_ra": self.associated_members_ra,
            "story_id": Decimal(str(self.story_id)) if self.story_id is not None else None,
            "description": self.description
        }
        
        data_without_none_values = {k: v for k, v in data.items() if v is not None}
        return data_without_none_values
    
    @staticmethod
    def from_dynamo(data: dict) -> "ActionDynamoDTO":
        return ActionDynamoDTO(
            owner_ra=data['owner_ra'],
            start_date=int(data['start_date']),
            stack_tags=[STACK(tag) for tag in data['stack_tags']],
            end_date=int(data['end_date']),
            duration=int(data['duration']),
            action_id=data['action_id'],
            is_valid=data['is_valid'],
            title=data['title'],
            project_code=data['project_code'],
            action_type_tag=ACTION_TYPE(data['action_type_tag']),
            associated_members_ra=data['associated_members_ra'],
            story_id=int(data['story_id']) if 'story_id' in data else None,
            description=data['description'] if 'description' in data else None
        )

    def to_entity(self) -> Action:
        return Action(
            owner_ra=self.owner_ra,
            start_date=self.start_date,
            stack_tags=self.stack_tags,
            end_date=self.end_date,
            duration=self.duration,
            action_id=self.action_id,
            is_valid=self.is_valid,
            title=self.title,
            project_code=self.project_code,
            action_type_tag=self.action_type_tag,
            associated_members_ra=self.associated_members_ra,
            story_id=self.story_id,
            description=self.description
        )
        
    def __repr__(self): 
        return f"Action(owner_ra={self.owner_ra}, start_date={self.start_date}, end_date={self.end_date}, action_id={self.action_id}, is_valid={self.is_valid}, title={self.title}, project_code={self.project_code}, associated_members_ra={self.associated_members_ra}, stack_tags={self.stack_tags}, action_type_tag={self.action_type_tag})"
    
    def __eq__(self, other):
        if type(other) != ActionDynamoDTO:
            return False
        return self.owner_ra == other.owner_ra and self.start_date == other.start_date and self.end_date == other.end_date and self.action_id == other.action_id and self.is_valid == other.is_valid and self.title == other.title and self.project_code == other.project_code and self.associated_members_ra == other.associated_members_ra and self.stack_tags == other.stack_tags and self.action_type_tag == other.action_type_tag
        
        