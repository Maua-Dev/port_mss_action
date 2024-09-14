from decimal import Decimal
from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserNotAllowed

from src.shared.domain.repositories.action_repository_interface import IActionRepository
from datetime import datetime


class GetAllMembersUsecase:
    def __init__(self, memberrepo: IMemberRepository, actionrepo: IActionRepository):
        self.memberrepo = memberrepo
        self.actionrepo = actionrepo
        
    def __call__(self,user_id: str) -> list:
        member = self.memberrepo.get_member(user_id)
        if member is None:
            raise NoItemsFound('user_id')
        

        is_active = Member.validate_active(member.active)
        

        members = self.memberrepo.get_all_members()

            
        if not is_active:
            raise UserNotAllowed()
        
        return members
