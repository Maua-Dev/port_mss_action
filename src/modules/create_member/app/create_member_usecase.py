import datetime
from typing import List
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class CreateMemberUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
    
    def __call__(self, member: Member) -> Member:
        
        if self.repo.get_member(ra=member.ra) is not None:
            raise DuplicatedItem('ra')
        
        return self.repo.create_member(member)
    