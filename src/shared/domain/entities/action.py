import abc
import datetime
from typing import List
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK

from src.shared.helpers.errors.domain_errors import EntityParameterTypeError, EntityError

class Action(abc.ABC):
    owner_ra: str
    date: datetime.datetime
    action_id: str
    title: str
    duration: datetime.time
    project_code: str
    associated_members_ra: List[str] = None
    stack_tags: List[STACK] = None
    action_type_tags: List[ACTION_TYPE] = None
    MIN_TITLE_LENGTH = 4
    MAX_TITLE_LENGTH = 100
    ACTION_ID_LENGTH = 4
    PROJECT_CODE_LENGTH = 2
    
    
    def __init__(self, owner_ra: str, date: datetime.datetime, action_id: str, associated_members_ra: List[str], title: str, duration: datetime.time, project_code: str, stack_tags: List[STACK], action_type_tags: List[ACTION_TYPE]):
        
        if not self.validate_ra(owner_ra):
            raise EntityError('owner_ra')
        self.owner_ra = owner_ra
        
        if type(date) != datetime.datetime:
            raise EntityError('date')
        self.date = date
        
        if not self.validate_action_id(action_id):
            raise EntityError('action_id')
        self.action_id = action_id
        
        if associated_members_ra is None:
            self.associated_members_ra = []
        elif type(associated_members_ra) == list:
            if not all([self.validate_ra(ra) for ra in associated_members_ra]):
                raise EntityError('associated_members_ra')
            else:
                self.associated_members_ra = associated_members_ra
        else:
            raise EntityError('associated_members_ra')
        
        if not self.validate_title(title):
            raise EntityError('title')
        self.title = title
        
        if type(duration) != datetime.time:
            raise EntityError('duration')
        self.duration = duration
        
        if not self.validate_project_code(project_code):
            raise EntityError('project_code')
        self.project_code = project_code
        
        
        if stack_tags is None:
            self.stack_tags = []
        elif type(stack_tags) == list:
            if not all([type(tag) == STACK for tag in stack_tags]):
                raise EntityError('stack_tags')
            else:
                self.stack_tags = stack_tags
        else:
            raise EntityError('stack_tags')
            
        
        if action_type_tags is None:
            self.action_type_tags = []
        elif type(action_type_tags) == list:
            if not all([type(tag) == ACTION_TYPE for tag in action_type_tags]):
                raise EntityError('action_type_tags')
            else:
                self.action_type_tags = action_type_tags
        else:
            raise EntityError('action_type_tags')

    def __repr__(self):
        return f'Action(owner_ra={self.owner_ra}, date={self.date}, action_id={self.action_id}, associated_members_ra={self.associated_members_ra}, title={self.title}, duration={self.duration}, project_code={self.project_code}, stack_tags={self.stack_tags}, action_type_tags={self.action_type_tags})'
    
    def __eq__(self, other):
        if type(other) != Action:
            return False
        return self.owner_ra == other.owner_ra and self.date == other.date and self.action_id == other.action_id and self.associated_members_ra == other.associated_members_ra and self.title == other.title and self.duration == other.duration and self.project_code == other.project_code and self.stack_tags == other.stack_tags and self.action_type_tags == other.action_type_tags
        
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
    
    @staticmethod
    def validate_project_code(project_code: str) -> bool:
        if type(project_code) != str:
            return False
        if len(project_code) != Action.PROJECT_CODE_LENGTH:
            return False
        return True
    
    