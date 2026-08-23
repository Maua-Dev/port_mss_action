from decimal import Decimal
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserIsNotFromAdmin, UserNotAllowed


class GetHoursChartUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member

    def __call__(self, user_id: str, start_date: Optional[int] = None, end_date: Optional[int] = None) -> Tuple[List[Project], Dict[str, int], Dict[str, Dict[str, int]]]:

        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()
        user = self.repo_member.get_member(user_id=user_id)

        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()

        is_allowed = Member.validate_role_admin(user.role) or user.stack in [STACK.BUSINESS, STACK.RH]
        if not is_allowed:
            raise UserIsNotFromAdmin()

        if start_date is None:
            if Environments.get_envs().stage.value == "TEST":
                now = datetime(2025, 12, 17)
                year = 2025
            else:
                now = datetime.now()
                year = now.year

            if (now.month <= 6) or (now.month == 12):
                if now.month <= 6:
                    start_date = datetime(year - 1, 12, 1).timestamp() * 1000
                else:
                    start_date = datetime(year, 12, 1).timestamp() * 1000
            else:
                start_date = datetime(year, 7, 1).timestamp() * 1000

        if end_date is None:
            if Environments.get_envs().stage.value == "TEST":
                now = datetime(2025, 12, 17)
                year = 2025
            else:
                now = datetime.now()
                year = now.year

            if (now.month <= 6) or (now.month == 12):
                if now.month <= 6:
                    end_date = datetime(year, 6, 30).timestamp() * 1000
                else:
                    end_date = datetime(year + 1, 6, 30).timestamp() * 1000
            else:
                end_date = datetime(year, 11, 30).timestamp() * 1000

        start_date, end_date = Decimal(start_date), Decimal(end_date)

        projects = self.repo.get_all_projects()

        hours_by_project = self.repo.get_all_actions_durations_by_project(start_date=start_date, end_date=end_date)

        hours_by_project_and_stack = self.repo.get_all_actions_durations_by_project_and_stack(start_date=start_date, end_date=end_date)

        return projects, hours_by_project, hours_by_project_and_stack