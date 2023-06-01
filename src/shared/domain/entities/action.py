
import abc
from typing import List
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError, EntityError

class Action(abc.ABC):
    owner_ra: str
    start_date: int # milisseconds
    end_date: int # milisseconds
    duration: int # milisseconds
    action_id: str
    story_id: int = None
    title: str
    description: str = None
    project_code: str
    associated_members_ra: List[str] = None
    stack_tags: List[STACK]
    action_type_tag: ACTION_TYPE
    MIN_TITLE_LENGTH = 4
    MAX_TITLE_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 500
    ACTION_ID_LENGTH = 4
    PROJECT_CODE_LENGTH = 2
    MIN_STORY_ID = 1
    MAX_STORY_ID = 999999

    
    
    def __init__(self, owner_ra: str, start_date: int, stack_tags: List[STACK], end_date: int, duration: int, action_id: str, title: str, project_code: str, action_type_tag: ACTION_TYPE, associated_members_ra: List[str] = None, description: str = None, story_id: int = None, ):
        
        if not self.validate_ra(owner_ra):
            raise EntityError('owner_ra')
        self.owner_ra = owner_ra
        
        if type(start_date) != int:
            raise EntityError('start_date')
        self.start_date = start_date
        
        if not self.validate_action_id(action_id):
            raise EntityError('action_id')
        self.action_id = action_id

        if not self.validate_story_id(story_id):
             raise EntityError('story_id')
        self.story_id = story_id
        
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
        
        if not self.validate_description(description):
            raise EntityError('description')
        self.description = description
        
        if type(end_date) != int:
            raise EntityError('end_date')
        if end_date < start_date:
            raise EntityError('start_date and end_date')
        self.end_date = end_date
        
        if not self.validate_duration(duration, start_date, end_date):
            raise EntityError('duration')
        self.duration = duration
        
        if not self.validate_project_code(project_code):
            raise EntityError('project_code')
        self.project_code = project_code
        
        if type(stack_tags) == list:
            if not all([type(tag) == STACK for tag in stack_tags]):
                raise EntityError('stack_tags')
            else:
                self.stack_tags = stack_tags
        else:
            raise EntityError('stack_tags')
    
        
        if type(action_type_tag) != ACTION_TYPE:
            raise EntityError('action_type_tag')
        self.action_type_tag = action_type_tag

    def __repr__(self):
        return f'Action(owner_ra={self.owner_ra}, start_date={self.start_date}, end_date={self.end_date}, action_id={self.action_id}, title={self.title}, project_code={self.project_code}, associated_members_ra={self.associated_members_ra}, stack_tags={self.stack_tags}, action_type_tag={self.action_type_tag.value()})'
    
    def __eq__(self, other):
        if type(other) != Action:
            return False
        return self.owner_ra == other.owner_ra and self.start_date == other.start_date and self.end_date == other.end_date and self.action_id == other.action_id and self.title == other.title and self.project_code == other.project_code and self.associated_members_ra == other.associated_members_ra and self.stack_tags == other.stack_tags and self.action_type_tag == other.action_type_tag
        
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
    def validate_story_id(story_id: int) -> bool:
        if story_id is not None:
            if type(story_id) != int:
                return False
            if story_id < Action.MIN_STORY_ID or story_id > Action.MAX_STORY_ID:
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
    def validate_description(description: str) -> bool:
        if description is not None:
            if type(description) != str:
                return False
            if len(description) < Action.MIN_TITLE_LENGTH or len(description) > Action.MAX_DESCRIPTION_LENGTH:
                return False
        return True
    
    @staticmethod
    def validate_project_code(project_code: str) -> bool:
        if type(project_code) != str:
            return False
        if len(project_code) != Action.PROJECT_CODE_LENGTH:
            return False
        return True
    
    @staticmethod
    def validate_duration(duration: int, start_date: int, end_date: int) -> bool:
        if type(duration) != int:
            return False
        if duration <= 0:
            return False
        if duration > end_date - start_date:
            return False
        return True