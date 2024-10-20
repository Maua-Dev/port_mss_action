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
        
    def __call__(self, user_id: str, start_date: Optional[int] = None, end_date: Optional[int] = None) -> list:
        member = self.memberrepo.get_member(user_id)
        if member is None:
            raise NoItemsFound('user_id')
        
        is_active = Member.validate_active(member.active)
        is_admin = Member.validate_role_admin(member.role)  # Verifica se o membro é admin

        if start_date is None:
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
        if is_admin:
            hours_worked = self.actionrepo.get_all_actions_durations_by_user_id(start_date, end_date)
        
        members = self.memberrepo.get_all_members()
        projects = self.actionrepo.get_all_projects()
        
        member_projects = {member.user_id: [] for member in members}
        
        for project in projects:
            project_name = project.name
            for member_user_id in project.members_user_ids:
                if member_user_id in member_projects:
                    member_projects[member_user_id].append(project_name)
                    
        for member in members:
            member_user_id = member.user_id
            member.hours_worked = hours_worked.get(member_user_id, 0) if is_admin else None
            member.project = member_projects[member_user_id]
        
        if not is_active:
            raise UserNotAllowed()
        
        return members
