from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetAllActionsByRaUsecase:
    
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> List[Action]:
        member = self.repo.get_member(ra=ra)
        
        if member == None:
            raise NoItemsFound('ra')
        
        return self.repo.get_all_actions_by_ra(ra=ra)