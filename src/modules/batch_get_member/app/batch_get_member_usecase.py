from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from typing import List
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class BatchGetMemberUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        

class BatchGetMemberUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo

    def __call__(self, ras: List[str]) -> List[Member]:
        members = self.repo.batch_get_member(ras=ras)
        
        if len(members) == 0:
            raise NoItemsFound('ras')
        
        unique_members = []
        for member in members:
            if member not in unique_members:
                unique_members.append(member)
            
        return unique_members