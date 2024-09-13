import abc
from typing import List, Optional
import uuid
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityParameterTypeError, EntityError

class Action(abc.ABC):
    user_id: str
    start_date: int # milisseconds
    end_date: int # milisseconds
    duration: int # milisseconds
    action_id: str
    is_valid: bool
    story_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    project_code: str
    associated_members_user_ids: List[str]
    stack_tags: List[STACK]
    action_type_tag: ACTION_TYPE
    MIN_TITLE_LENGTH = 4
    MAX_TITLE_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 500
    ACTION_ID_LENGTH = 36
    PROJECT_CODE_LENGTH = 2
    MIN_STORY_ID = 1
    MAX_STORY_ID = 999999
    USER_ID_LENGTH = 36

    
    
    def __init__(self, user_id: str, start_date: int, stack_tags: List[STACK], end_date: int, duration: int, action_id: str, is_valid: bool, title: str, project_code: str, action_type_tag: ACTION_TYPE, associated_members_user_ids: List[str] = [], description: Optional[str] = None, story_id: Optional[int] = None):
        
        if not self.validate_user_id(user_id):
            raise EntityError('user_id')
        self.user_id = user_id
        
        if type(start_date) != int:
            raise EntityError("start_date")
        if not 1000000000000 < start_date < 10000000000000:
            raise EntityError("start_date")
        self.start_date = start_date
        
        if not self.validate_action_id(action_id):
            raise EntityError('action_id')
        self.action_id = action_id

        if type(is_valid) != bool:
            raise EntityError('is_valid')
        self.is_valid = is_valid

        if not self.validate_story_id(story_id):
             raise EntityError('story_id')
        self.story_id = story_id
        
        if type(associated_members_user_ids) == list:
            if not all([self.validate_user_id(user_id) for user_id in associated_members_user_ids]):
                print("Teste1")
                raise EntityError('associated_members_user_ids')
            if user_id in associated_members_user_ids:
                print("Teste2")
                raise EntityError('associated_members_user_ids')
            if len(associated_members_user_ids) != len(set(associated_members_user_ids)):
                print("Teste3")
                raise EntityError('associated_members_user_ids')
            else:
                self.associated_members_user_ids = associated_members_user_ids
        else:
            print("Teste4")
            raise EntityError('associated_members_user_ids')
        
        if not self.validate_title(title):
            raise EntityError('title')
        self.title = title
        
        if not self.validate_description(description):
            raise EntityError('description')
        self.description = description
        
        if type(end_date) != int:
            raise EntityError("end_date")
        if not 1000000000000 < end_date < 10000000000000:
            raise EntityError("end_date")
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
        return f'Action(user_id={self.user_id}, start_date={self.start_date}, end_date={self.end_date}, action_id={self.action_id}, is_valid={self.is_valid} title={self.title}, project_code={self.project_code}, associated_members_user_ids={self.associated_members_user_ids}, stack_tags={self.stack_tags}, action_type_tag={self.action_type_tag.value})'
    
    def __eq__(self, other):
        if type(other) != Action:
            return False
        return self.user_id == other.user_id and self.start_date == other.start_date and self.end_date == other.end_date and self.action_id == other.action_id and self.is_valid == other.is_valid and self.title == other.title and self.project_code == other.project_code and self.associated_members_user_ids == other.associated_members_user_ids and self.stack_tags == other.stack_tags and self.action_type_tag == other.action_type_tag
        
    
    @staticmethod
    def validate_action_id(action_id: str) -> bool:
        if type(action_id) != str:
            return False
        if len(action_id) != Action.ACTION_ID_LENGTH:
            return False
        try:
            uuid.UUID(action_id)
            return True
        except ValueError:
            return False

    
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
    
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str: return False
        if len(user_id) != Action.USER_ID_LENGTH: return False
        return True