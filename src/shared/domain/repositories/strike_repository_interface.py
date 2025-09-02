from abc import ABC, abstractmethod
from typing import List, Optional
from src.shared.domain.entities.strike import Strike



class IStrikeRepository(ABC):

    @abstractmethod
    def create_strike(self, strike: Strike) -> Strike:
        '''
        Creates a new strike.
        '''
        pass

    @abstractmethod
    def get_all(self) -> List[Strike]:
        '''
        returns all strikes.
        '''
        pass

    @abstractmethod
    def find_by_id(self, strike_id: str) -> Optional[Strike]:
        '''
        Finds a strike by its ID.
        If there is no strike with the given ID, return None.
        '''
        pass

    @abstractmethod
    def delete_strike(self, strike_id: str) -> Optional[Strike]:
        '''
        Deletes a strike by its ID.
        If there is no strike with the given ID, return None.
        '''
        pass

