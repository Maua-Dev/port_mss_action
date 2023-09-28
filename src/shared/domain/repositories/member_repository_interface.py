from abc import ABC, abstractmethod
from tkinter import ACTIVE
from typing import List, Optional, Tuple
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
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
    def delete_member(self, ra: str) -> Optional[Member]:
        '''
        If member exists, deletes it and returns it
        else returns None
        '''
        pass

    @abstractmethod
    def update_member(self, ra: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_email: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None, new_hired_date: Optional[int] = None, new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None) -> Member:
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
    def get_member(self, ra: str) -> Member:
        '''
        If member exists, returns it
        else returns None
        '''
        pass

    @abstractmethod
    def batch_get_member(self, ras: List[str]) -> List[Member]:
        '''
        Returns all members with the given ras, if any
        else returns []
        '''
        pass