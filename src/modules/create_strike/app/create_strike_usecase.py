from typing import Optional
import uuid
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserIsNotFromRH


class CreateStrikeUsecase:
    def __init__(self, repo: IStrikeRepository, repo_member: IMemberRepository):
        self.repo= repo
        self.repo_member= repo_member

    def __call__(self, owner_user_id: str, target_user_id: str,applier_user_id: str, occurred_date: int, category: STRIKE_CATEGORY,description: Optional [str] = None) -> Strike:

        strike_id= str(uuid.uuid4())

        Strike(
            strike_id= strike_id,
            owner_user_id= owner_user_id,
            target_user_id= target_user_id,
            applier_user_id= applier_user_id,
            occurred_date= occurred_date,
            category= category,
            description= description
        )

        if self.repo_member.get_member(user_id=owner_user_id) is None or self.repo_member.get_member(user_id=applier_user_id) is None or self.repo_member.get_member(user_id=target_user_id) is None:
            raise UnregisteredUser()
        
        applier_user= self.repo_member.get_member(user_id=applier_user_id)

        if applier_user.active != ACTIVE.ACTIVE:
            raise ForbiddenAction("RH member is not active")
        
        if applier_user.role not in [ROLE.DIRECTOR, ROLE.INTERNAL]:
            raise UserIsNotFromRH()

        if applier_user.stack is not STACK.RH:
            raise UserIsNotFromRH()
        
        target_user= self.repo_member.get_member(user_id=target_user_id)

        if target_user.active != ACTIVE.ACTIVE:
            raise ForbiddenAction('target user is not active')
        
        
        





