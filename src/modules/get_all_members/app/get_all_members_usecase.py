from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
class GetAllMembersUsecase:
    def __init__(self, memberrepo: IMemberRepository, actionrepo: IActionRepository):
        self.memberrepo = memberrepo
        self.actionrepo = actionrepo
        
    def __call__(self,user_id: str, start_date: Optional[int] = 1719802860000, end_date: Optional[int] = 1735700340000) -> list:
        member = self.memberrepo.get_member(user_id)
        if member is None:
            raise NoItemsFound('user_id')
        
        members = self.memberrepo.get_all_members()
        is_active = Member.validate_active(member.active)
        hours_worked = self.actionrepo.get_all_actions_durations_by_user_id(start_date, end_date)
        
        for member in members:
            member_user_id = member.user_id
            member.hours_worked = hours_worked.get(member_user_id, 0)
            
        if not is_active:
            raise ForbiddenAction('user. This user is not active.') 
        return members