from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserNotAllowed


class DeleteMemberUseCase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    
    def __call__(self, user_id: str, member_user_id: Optional[str] = None) -> Optional[Member]:
        if not self.repo.get_member(user_id=user_id):
            raise EntityError('user_id')
        
        if (member_user_id is not None) and (not self.repo.get_member(user_id=member_user_id)):
            raise EntityError('member_user_id')
        
        user = self.repo.get_member(user_id=user_id)
        
        is_active = Member.validate_active(user.active)
        
        if not is_active:
            raise ForbiddenAction('user. This user is not active.')
        
        is_admin = Member.validate_role_admin(user.role)

        if is_admin and member_user_id is None:
            member = self.repo.delete_member(user_id=user_id)
        elif is_admin and member_user_id is not None:
            member = self.repo.delete_member(user_id=member_user_id)
        elif not is_admin and member_user_id is None:
            member = self.repo.delete_member(user_id=user_id)
        else:
            raise UserNotAllowed()

        if member is None:
            raise NoItemsFound('user_id')
        
        return member