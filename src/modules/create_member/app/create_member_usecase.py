from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active import ACTIVE
from src.shared.domain.enums.course import COURSE
from src.shared.domain.enums.role import ROLE
from src.shared.domain.enums.stack import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.domain_errors import DuplicatedItem
import datetime

class CreateMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self, ra: str, name: str, email_dev: str , email: str, role: ROLE, stack: STACK, year: int, cellphone: str, course: COURSE, user_id:str, photo: Optional[str] = None) -> Member:
        
        if self.repo.get_member(user_id=user_id) is not None:
            raise DuplicatedItem("user_id")

        name_title = name.title()
        
        member = Member(name=name_title, email_dev=email_dev, email=email, ra=ra, role=role, stack=stack, year=year, cellphone=cellphone, course=course, active=ACTIVE.ON_HOLD, user_id=user_id,  deactivated_date=None, hired_date = int(datetime.datetime.now().timestamp() * 1000), photo=photo)           
         
        return self.repo.create_member(member)