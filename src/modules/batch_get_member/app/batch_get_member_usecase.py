from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from typing import List
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser


class BatchGetMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        

class BatchGetMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo

    def __call__(self, user_id: str, user_ids: List[str]) -> List[Member]:
        member = self.repo.get_member(user_id=user_id)
        
        if member == None:
            raise UnregisteredUser()
        
        user_ids = list(set(user_ids))
        members = self.repo.batch_get_member(user_ids=user_ids)
        
        if len(members) == 0:
            raise NoItemsFound('user_ids')
        
        is_active = Member.validate_active(member.active)
        
        if not is_active:
            raise ForbiddenAction('user. This user is not active.')
            
        return members