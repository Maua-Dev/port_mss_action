from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project


class IActionRepository(ABC):
    
    
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
    
    @abstractmethod
    def create_project(self, project: Project) -> Project:
        '''
        If project does not exist, creates it and returns it
        else returns None
        '''
        pass
    
    @abstractmethod
    def delete_project(self, code: str) -> Optional[Project]:
        '''
        If project exists, deletes it and returns it
        else returns None
        '''
        pass
    
    @abstractmethod
    def get_members_by_project(self, code: str) -> Optional[List[Member]]:
        '''
        Returns all members associated to the project with the given code, if any
        else returns []
        '''
        pass
    
    @abstractmethod
    def get_project(self, code: str) -> Optional[Tuple[Project, List[Member]]]:
        '''
        If project exists, returns it with its members
        else returns None
        '''
        pass