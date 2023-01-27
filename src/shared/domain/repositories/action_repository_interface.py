from abc import ABC, abstractmethod
from typing import List
from src.shared.domain.entities.member import Member


class IActionRepository(ABC):

    @abstractmethod
    def get_member(self, ra: str) -> Member:
        pass
    