from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member


class IActionRepository(ABC):

    @abstractmethod
    def get_member(self, ra: str) -> Member:
        pass
    
    @abstractmethod
    def get_all_actions_by_ra(self, ra: str) -> List[Action]:
        '''
        return [] if member doesn't have actions
        '''
        pass
    
    @abstractmethod
    def create_member(self, member: Member) -> Member:
        pass