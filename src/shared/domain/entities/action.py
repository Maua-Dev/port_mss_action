
import abc
from typing import List
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError, EntityError

class Action(abc.ABC):
    owner_ra: str
    start_time: int # milisseconds
    end_time: int # milisseconds
    action_id: str
    title: str
    project_code: str
    associated_members_ra: List[str] = None
    stack_tags: List[STACK] = None
    action_type_tags: List[ACTION_TYPE] = None
    MIN_TITLE_LENGTH = 4
    MAX_TITLE_LENGTH = 100
    ACTION_ID_LENGTH = 4
    PROJECT_CODE_LENGTH = 2
    
    
    def __init__(self, owner_ra: str, start_time: int, end_time: int, action_id: str, title: str, project_code: str, associated_members_ra: List[str] = None, stack_tags: List[STACK] = None, action_type_tags: List[ACTION_TYPE] = None):
        
        if not self.validate_ra(owner_ra):
            raise EntityError('owner_ra')
        self.owner_ra = owner_ra
        
        if type(start_time) != int:
            raise EntityError('start_time')
        self.start_time = start_time
        
        if not self.validate_action_id(action_id):
            raise EntityError('action_id')
        self.action_id = action_id
        
        if associated_members_ra is None:
            self.associated_members_ra = []
        elif type(associated_members_ra) == list:
            if not all([self.validate_ra(ra) for ra in associated_members_ra]):
                raise EntityError('associated_members_ra')
            if owner_ra in associated_members_ra:
                raise EntityError('associated_members_ra')
            if len(associated_members_ra) != len(set(associated_members_ra)):
                raise EntityError('associated_members_ra')
            else:
                self.associated_members_ra = associated_members_ra
        else:
            raise EntityError('associated_members_ra')
        
        if not self.validate_title(title):
            raise EntityError('title')
        self.title = title
        
        if type(end_time) != int:
            raise EntityError('end_time')
        if end_time < start_time:
            raise EntityError('start_time and end_time')
        self.end_time = end_time
        
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
        return f'Action(owner_ra={self.owner_ra}, start_time={self.start_time}, end_time={self.end_time}, action_id={self.action_id}, title={self.title}, project_code={self.project_code}, associated_members_ra={self.associated_members_ra}, stack_tags={self.stack_tags}, action_type_tags={self.action_type_tags})'
    
    def __eq__(self, other):
        if type(other) != Action:
            return False
        return self.owner_ra == other.owner_ra and self.start_time == other.start_time and self.end_time == other.end_time and self.action_id == other.action_id and self.title == other.title and self.project_code == other.project_code and self.associated_members_ra == other.associated_members_ra and self.stack_tags == other.stack_tags and self.action_type_tags == other.action_type_tags
        
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
    
    