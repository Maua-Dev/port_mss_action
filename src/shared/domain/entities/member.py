import abc
import datetime
import re
from typing import List
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE

from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError


class Member(abc.ABC):
    name: str
    email: str
    ra: str
    role: ROLE
    stack: STACK
    year: int
    cellphone: str
    course: COURSE
    hired_date: datetime.datetime
    active: ACTIVE
    projects: List[Project]
    MIN_NAME_LENGTH = 2
    CELLPHONE_LENGTH = 11

    def __init__(self,
                 name:str,
                 email:str,
                 ra:str,
                 role:ROLE,
                 stack:STACK,
                 year:int,
                 cellphone:str,
                 course: COURSE,
                 hired_date: datetime.datetime,
                 active: ACTIVE,
                 projects: List[Project] = None
                ):

        if not Member.validate_name(name):
            raise EntityError('name')
        self.name = name
        
        if not Member.validate_ra(ra):
            raise EntityError('ra')
        self.ra = ra

        if not Member.validate_email(email):
            raise EntityError('email')
        self.email = email
        
        if type(role) != ROLE:
            raise EntityError("role")
        self.role = role
        
        if type(stack) != STACK:
            raise EntityError("stack")
        self.stack = stack
        
        if type(year) != int:
            raise EntityError("year")
        self.year = year
        
        if not Member.validate_cellphone(cellphone):
            raise EntityError("cellphone")
        self.cellphone = cellphone
        
        if type(course) != COURSE:
            raise EntityError("course")
        self.course = course
        
        if type(hired_date) != datetime.datetime:
            raise EntityError("active")
        self.hired_date = hired_date
        
        if type(active) != ACTIVE:
            raise EntityError("active")
        self.active = active
        
        if projects is None:
            self.projects = []
        elif type(projects) == list:
            if not all([type(project) == Project for project in projects]):
                raise EntityError("projects")
            else:
                self.projects = projects
        else:
            raise EntityError("projects")

                
    @staticmethod
    def validate_ra(ra: str) -> bool:
        if ra == None:
            return False

        if type(ra) != str:
            raise EntityParameterTypeError('ra must be a string')

        return ra.isdecimal() and len(ra) == 8

    @staticmethod
    def validate_email(email) -> bool:
        if email == None:
            return False
        if type(email) != str:
            return False
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_name(name) -> bool:

        if type(name) != str:
            return False
        
        if len(name) < Member.MIN_NAME_LENGTH:
            return False

        return True
    
    @staticmethod
    def validate_cellphone(cellphone) -> bool:
        if type(cellphone) != str:
            return False
        
        if len(cellphone) != Member.CELLPHONE_LENGTH:
            return False
        
        return True
        
    @staticmethod
    def validate_project_code(code: str) -> bool:
        if type(code) != str:
            return False
        
        if len(code) != Project.PROJECT_CODE_LENGTH:
            return False
        
        if not code.isupper() and not code.isalpha():
            return False
        
        return True
        