
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
        
    def __call__(self, ra: str, name: str, email_dev: str , email: str, role: ROLE, stack: STACK, year: int, cellphone: str, course: COURSE, hired_date: int, user_id:str) -> Member:
      
        

        
        member = Member( name, email_dev, email,ra, role, stack, year, cellphone, course, hired_date, ACTIVE.ACTIVE,user_id,None)        
        
        self.repo.create_member(member)
        
        
        return member