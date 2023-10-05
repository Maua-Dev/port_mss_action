
from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self, ra: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None,  new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None) -> Member:
        
        if not Member.validate_ra(ra):
            raise EntityError("ra")


        member = self.repo.get_member(ra)
        if not member:
            raise NoItemsFound('member')
        
           

        return self.repo.update_member(ra, new_name, new_email_dev, new_role, new_stack, new_year, new_cellphone, new_course, new_deactivated_date, new_active)