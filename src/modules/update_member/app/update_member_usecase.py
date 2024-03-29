
from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UpdateMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
        
    def __call__(self, user_id: str, new_name: Optional[str] = None, new_email_dev: Optional[str] = None, new_role: Optional[ROLE] = None, new_stack: Optional[STACK] = None, new_year: Optional[int] = None, new_cellphone: Optional[str] = None, new_course: Optional[COURSE] = None,  new_deactivated_date: Optional[int] = None, new_active: Optional[ACTIVE] = None) -> Member:
        
        if not Member.validate_user_id(user_id):
            raise EntityError("user_id")


        member = self.repo.get_member(user_id)
        if not member:
            raise NoItemsFound('member')
        
        
 
        if new_name is not None:
            if type(new_name) is not str:
                raise EntityError("new_name")

        if new_email_dev is not None:
            if type(new_email_dev) is not str:
                raise EntityError('new_email_dev')
            if not Member.validate_email_dev(new_email_dev):
                raise EntityError('new_email_dev')

        if new_role is not None:
            if type(new_role) is not ROLE:
                raise EntityError('new_role')



        if new_stack is not None:
            if type(new_stack) is not STACK:
                raise EntityError('new_stack')



        

        if new_year is not None:
            if type(new_year) is not int:
                raise EntityError('new_year')
            if new_year < 1 or new_year>6:
                raise EntityError('new_year')

        if new_cellphone is not None:
            if type(new_cellphone) is not str:
                 raise EntityError('new_cellphone')
            
            if not Member.validate_cellphone(new_cellphone):
                raise EntityError('new_cellphone')

        if new_course is not None:
            if type(new_course) is not COURSE:
                 raise EntityError('new_course')


        if new_deactivated_date is not None:
            if type(new_deactivated_date) is not int:
                raise EntityError('new_deactivated_date')
            if new_deactivated_date < 0 or new_deactivated_date<member.hired_date:
                raise EntityError('new_deactivated_date')

        if new_active is not None:
            if type(new_active) is not ACTIVE:
                raise EntityError('new_active')

        return self.repo.update_member(user_id, member.hired_date,member.email,new_name, new_email_dev, new_role, new_stack, new_year, new_cellphone, new_course, new_deactivated_date, new_active)