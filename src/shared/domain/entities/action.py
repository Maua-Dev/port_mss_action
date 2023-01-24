import abc
import datetime
from typing import List

from src.shared.helpers.errors.domain_errors import EntityParameterTypeError, EntityError

class Action(abc.ABC):
    owner_ra: str
    date: datetime.datetime
    action_id: str
    associated_members_ra: List[str] = None
    title: str
    duration: datetime.time
    project_code: str
    tags: List[str]
    MIN_TITLE_LENGTH = 4
    MAX_TITLE_LENGTH = 100
    ACTION_ID_LENGTH = 4
    
    def __init__(self, owner_ra: str, date: datetime.datetime, action_id: str, associated_members_ra: List[str], title: str, duration: datetime.time, project_code: str, tags: List[str]):
        
        if not self.validate_ra(owner_ra):
            raise EntityError('owner_ra')
        self.owner_ra = owner_ra
        
        if type(date) != datetime.datetime:
            raise EntityError('date')
        self.date = date
        
        if not self.validate_action_id(action_id):
            raise EntityError('action_id')
        self.action_id = action_id
        
        if not all([self.validate_ra(ra) for ra in associated_members_ra]):
            raise EntityError('associated_members_ra')
        self.associated_members_ra = associated_members_ra
        
        if not self.validate_title(title):
            raise EntityError('title')
        self.title = title
        
        if type(duration) != datetime.time:
            raise EntityError('duration')
        self.duration = duration
        
        if type(project_code) != str:
            raise EntityError('project_code')
        self.project_code = project_code
        
        if not all([type(tag) == str for tag in tags]):
            raise EntityError('tags')
        self.tags = tags
        
    def __repr__(self):
        return f"Action(owner_ra={self.owner_ra}, date={self.date}, action_id={self.action_id}, associated_members_ra={self.associated_members_ra}, title={self.title}, duration={self.duration}, project_code={self.project_code}, tags={self.tags})"
    
    def __eq__(self, other):
        if type(other) != Action:
            return False
        return self.owner_ra == other.owner_ra and self.date == other.date and self.action_id == other.action_id and self.associated_members_ra == other.associated_members_ra and self.title == other.title and self.duration == other.duration and self.project_code == other.project_code and self.tags == other.tags
        
    @staticmethod
    def validate_ra(ra: str) -> bool:
        if ra == None:
            return False

        if type(ra) != str:
            raise EntityParameterTypeError('ra must be a string')

        return ra.isdecimal() and len(ra) == 8
    
    @staticmethod
    def validate_action_id(action_id: str) -> bool:
        if type(action_id) != str:
            return False
        if len(action_id) != Action.ACTION_ID_LENGTH:
            return False
        return True
    
    @staticmethod
    def validate_title(title: str) -> bool:
        if type(title) != str:
            return False
        if len(title) < Action.MIN_TITLE_LENGTH or len(title) > Action.MAX_TITLE_LENGTH:
            return False
        return True
    
    