from datetime import datetime
from decimal import Decimal
from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser


class GetMemberUsecase:
    def __init__(self, member_repo: IMemberRepository, action_repo: IActionRepository):
        self.member_repo = member_repo
        self.action_repo = action_repo
        
    def __call__(self,user_id: str, start_date: Optional[int] = None, end_date: Optional[int] = None) -> Member:
    
        if not Member.validate_user_id(user_id):
            raise EntityError('user_id')
        
        member = self.member_repo.get_member(user_id=user_id)

        if member == None:
            raise UnregisteredUser()
        
        is_active = Member.validate_active(member.active)
        
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

        start_date, end_date = Decimal(start_date), Decimal(end_date)

        hours_worked = self.action_repo.get_all_actions_durations_by_user_id(start_date, end_date)
        
        member_user_id = member.user_id
        member.hours_worked = hours_worked.get(member_user_id, 0)
        
        if not is_active:
            raise ForbiddenAction('user. This user is not active.')
        
        return member