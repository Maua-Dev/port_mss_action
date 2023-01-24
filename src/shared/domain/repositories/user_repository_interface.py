from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        """
        If user not found raise NoItemsFound
        """
        pass

    