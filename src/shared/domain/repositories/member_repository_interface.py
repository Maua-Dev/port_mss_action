from abc import ABC, abstractmethod
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.strike import Strike
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
    def update_member(self, user_id: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None,new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None, new_photo: Optional[bytes] = None) -> Member:
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
    def get_active_heads_and_directors(self) -> List[Member]:
        '''
        It returns a list of the active members that have HEAD's or DIRECTOR's ROLE 
        '''
        pass

    @abstractmethod
    def batch_get_member(self, user_ids: List[str]) -> List[Member]:
        '''
        Returns all members with the given ras, if any
        else returns []
        '''
        pass

    @abstractmethod
    def send_active_member_email(self, member: Member) -> bool:
        """
        When a member's action is invalidated, notify the member and return True.
        Only in real repo
        """
        pass

    @abstractmethod
    def send_email_to_warn_about_member_reached_total_strike_limit(self, created_strike: Strike, strike_limit: int) -> bool:
        """
        When a member reach the total of stikes he can have, notify Dev's Heads and return True.
        Only in real repo
        """
        pass