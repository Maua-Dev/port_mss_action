from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteMemberUseCase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    
    def __call__(self, user_id: str) -> Optional[Member]:
        if not Member.validate_user_id(user_id=user_id):
            raise EntityError('user_id')
        
        member = self.repo.delete_member(user_id=user_id)
        
        if member is None:
            raise NoItemsFound('user_id')
        
        return member