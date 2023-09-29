
from typing import List, Optional
import uuid
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound

class CreateMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self, ra: str, name: Optional[str] = None, email_dev: Optional[str] = None, email: Optional[str] = None, role: Optional[ROLE] = None, stack: Optional[STACK] = None, year: Optional[int] = None, cellphone: Optional[str] = None, course: Optional[COURSE] = None, hired_date: Optional[int] = None, deactivated_date: Optional[int] = None, active: Optional[ACTIVE] = None) -> Member:
      
        
        # for ra in [owner_ra] + associated_members_ra:
        #     if not self.repo.get_member(ra):
        #         raise NoItemsFound(ra)
        
        member = Member( name, email_dev, email,ra, role, stack, year, cellphone, course, hired_date,  active,deactivated_date)        
        
        self.repo.create_member(member)
        
        
        return member