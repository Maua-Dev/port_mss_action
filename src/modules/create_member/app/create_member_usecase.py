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
    
    def __call__(self, name: str, email: str, ra: str, role: ROLE, stack: STACK, year: int, cellphone: str, course: COURSE, hired_date: datetime.datetime, active: ACTIVE, projects = None, deactivated_date = None) -> Member:
        
        if self.repo.get_member(ra=ra) is not None:
            raise DuplicatedItem('ra')
        
        if not Member.validate_name(name):
            raise EntityError('name')
        
        if not Member.validate_email_dev(email):
            raise EntityError('email')
        
        if not Member.validate_ra(ra):
            raise EntityError('ra')
        
        if type(role) is not ROLE:
            raise EntityError('role')
        
        if type(stack) is not STACK:
            raise EntityError('stack')
        
        if not Member.validate_year(year):
            raise EntityError('year')
        
        if not Member.validate_cellphone(cellphone):
            raise EntityError('cellphone')
        
        if type(course) is not COURSE:
            raise EntityError('course')
        
        if type(hired_date) is not datetime.datetime:
            raise EntityError('hired_date')
        
        if type(active) is not ACTIVE:
            raise EntityError('active')
        
        if projects is not None:
            if type(projects) is not list or not all(type(project) is Project for project in projects):
                raise EntityError('projects')
            projects == []
        
        if deactivated_date is not None and type(deactivated_date) is not datetime.datetime:
            raise EntityError('deactivated_date')
        
        member = Member(name=name, email=email, ra=ra, role=role, stack=stack, year=year, cellphone=cellphone, course=course, hired_date=hired_date, active=active, projects=projects, deactivated_date=deactivated_date)
        
        return self.repo.create_member(member)