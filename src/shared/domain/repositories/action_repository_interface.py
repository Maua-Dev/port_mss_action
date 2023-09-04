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
    def get_action(self, action_id: str) -> Optional[Action]:
        '''
        If action exists, returns it
        else returns None
        '''
        pass
    
    @abstractmethod
    def create_associated_action(self, associatedAction: AssociatedAction) -> AssociatedAction:
        '''
        append associated_action to associated_actions
        '''
        pass
    
    @abstractmethod
    def create_project(self, project: Project) -> Project:
        '''
        If project does not exist, creates it and returns it
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
    def get_project(self, code: str) -> Project:
        '''
        If project exists, returns it
        else returns None
        '''
        pass

    @abstractmethod
    def update_project(self, code: str, name: str, description: str, po_RA: str, scrum_RA: str, start_date: int, photos: List[str] = []) -> Project:
        '''
        If project exists, updates it and returns it
        else returns None
        '''
        pass
    
    def get_all_projects(self) -> List[Project]:
        '''
        Returns all projects
        '''
        pass
    
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
    def get_associated_actions_by_ra(self, ra: str, amount: int, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None) -> Tuple[List[AssociatedAction], Optional[dict]]:
        '''
        Retrieves all associated actions of a member, filtered by an optional time range specified by start and end parameters. The method allows for pagination using the exclusive_start_key parameter to determine the starting point of the action list, and the amount parameter to determine the maximum number of actions to be retrieved.
        If no actions are found, returns []
        '''
        pass
    
    @abstractmethod
    def batch_get_action(self, action_ids: List[str]) -> List[Action]:
        '''
        Returns all actions with the given ids, if any
        else returns []
        '''
        pass
    
    @abstractmethod
    def batch_update_associated_action_start(self, action_id: str, new_start_date: Optional[int] = None) -> List[AssociatedAction]:
        '''
        Updates all associated actions with new_start_date and returns them, if any
        '''
        pass
    
    @abstractmethod
    def batch_update_associated_action_members(self, action_id: str, members: List[str], start_date: int) -> List[AssociatedAction]:
        '''
        Removes all associated actions with action_id and recreates them with the given members and start_date
        '''
        pass
    
    @abstractmethod
    def update_action(self, action_id: str, new_owner_ra: Optional[str] = None, new_start_date : Optional[int] = None, new_end_date : Optional[int] = None, new_duration : Optional[int] = None, new_story_id : Optional[str] = None, new_title : Optional[str] = None, new_description : Optional[str] = None, new_project_code : Optional[str] = None, new_associated_members_ra : Optional[List[str]] = None, new_stack_tags : Optional[List[str]] = None, new_action_type_tag : Optional[str] = None) -> Action:
        '''
        If action exists, updates it and its associated actions and returns it
        else returns None
        '''
        pass