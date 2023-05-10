from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member


class IActionRepository(ABC):
    
    @abstractmethod
    def get_all_actions_by_ra(self, ra: str) -> List[Action]:
        '''
        return [] if member doesn't have actions
        '''
        pass
    
    @abstractmethod
    def create_action(self, action: Action) -> Action:
        '''
        creates action and associated_actions for each associated_member and the owner
        '''
        pass
    
    @abstractmethod
    def get_action(self, action_id: str) -> Action:
        pass
    
    @abstractmethod
    def create_associated_action(self, associatedAction: AssociatedAction) -> AssociatedAction:
        pass
    