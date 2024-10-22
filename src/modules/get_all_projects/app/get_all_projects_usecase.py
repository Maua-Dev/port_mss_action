from decimal import Decimal
from typing import Optional
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import UnregisteredUser,ForbiddenAction, UserNotAllowed
from src.shared.domain.enums.active_enum import ACTIVE
from datetime import datetime

class GetAllProjectsUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str, start_date: Optional[int] = None, end_date: Optional[int] = None) -> list:
        
        if self.repo_member.get_member(user_id) is None:
            raise UnregisteredUser()
        user = self.repo_member.get_member(user_id=user_id)
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()
        projects = self.repo.get_all_projects()

        is_admin = user.validate_role_admin(user.role)

        if not is_admin:
            raise ForbiddenAction("user. This user is not from admin")

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

        hours_worked = self.repo.get_all_actions_durations_by_project(start_date=start_date, end_date=end_date)
        
        projects = self.repo.get_all_projects()
          
        for project in projects:
            project_code = project.code
            project.hours_worked = hours_worked.get(project_code, 0)

        return projects