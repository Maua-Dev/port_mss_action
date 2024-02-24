from abc import ABC, abstractmethod
from src.shared.domain.enums.active_enum import ACTIVE
from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK


class IMemberRepository(ABC):
    
    
    @abstractmethod
    def create_member(self, member: Member) -> Member:
        '''
        creates member
        '''
        pass
    

    @abstractmethod
    def delete_member(self, user_id: str) -> Optional[Member]:
        '''
        If member exists, deletes it and returns it
        else returns None
        '''
        pass

    @abstractmethod
    def update_member(self, user_id: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None,  new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None) -> Member:
        '''
        If member exists, updates it and its associated actions and returns it
        else returns None
        '''
        pass

    @abstractmethod
    def get_all_members(self) -> List[Member]:
        '''
        Returns all members
        '''
        pass

    @abstractmethod
    def get_member(self, user_id: str) -> Member:
        '''
        If member exists, returns it
        else returns None
        '''
        pass

    @abstractmethod
    def batch_get_member(self, user_ids: List[str]) -> List[Member]:
        '''
        Returns all members with the given ras, if any
        else returns []
        '''
        pass