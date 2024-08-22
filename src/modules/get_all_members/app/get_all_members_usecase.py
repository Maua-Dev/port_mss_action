from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from datetime import datetime

class GetAllMembersUsecase:
    def __init__(self, memberrepo: IMemberRepository, actionrepo: IActionRepository):
        self.memberrepo = memberrepo
        self.actionrepo = actionrepo
        
    def __call__(self,user_id: str, start_date: Optional[int] = None, end_date: Optional[int] = None) -> list:
        member = self.memberrepo.get_member(user_id)
        if member is None:
            raise NoItemsFound('user_id')
        

        if start_date is None :
            now = datetime.now()
            year = now.year

            if now.month <= 6: 
                start_date = datetime(year, 1, 1).timestamp() * 1000
            else:  
                start_date = datetime(year, 7, 1).timestamp() * 1000
        

        if end_date is None:
            now = datetime.now()
            year = now.year

            if now.month <= 6: 
                end_date = datetime(year, 6, 30).timestamp() * 1000
            else:  
                end_date = datetime(year, 12, 31).timestamp() * 1000


        members = self.memberrepo.get_all_members()

        is_active = Member.validate_active(member.active)
        hours_worked = self.actionrepo.get_all_actions_durations_by_user_id(start_date, end_date)
        
        for member in members:
            member_user_id = member.user_id
            member.hours_worked = hours_worked.get(member_user_id, 0)
            
        if not is_active:
            raise ForbiddenAction('user. This user is not active.') 
        
        return members
