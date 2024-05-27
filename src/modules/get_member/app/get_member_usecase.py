from typing import Any
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class GetMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self, user_id: str) -> Member:
       

        if not Member.validate_user_id(user_id):
            raise EntityError('user_id')
        
        member = self.repo.get_member(user_id=user_id)

        if member == None:
            raise NoItemsFound('user_id')
        
        is_active = Member.validate_active(member.active)
        
        if not is_active:
            raise ForbiddenAction('user. This user is not active.')
        
        return member