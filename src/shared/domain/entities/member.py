import abc
import re
from typing import List, Optional
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError


class Member(abc.ABC):
    name: str
    email_dev: str
    email: str
    ra: str
    role: ROLE
    stack: STACK
    year: int
    cellphone: str
    course: COURSE
    hired_date: int # milliseconds
    deactivated_date: Optional[int] = None # milliseconds
    active: ACTIVE
    user_id: str
    photo: Optional[str] = None
    MIN_NAME_LENGTH = 2
    CELLPHONE_LENGTH = 11
    USER_ID_LENGTH = 36

    def __init__(self,
                 name:str,
                 email_dev:str,
                 email:str,
                 ra:str,
                 role:ROLE,
                 stack:STACK,
                 year:int,
                 cellphone:str,
                 course: COURSE,
                 hired_date: int,
                 active: ACTIVE,
                 user_id: str,
                 photo: Optional[str] = None,
                 deactivated_date: Optional[int] = None
                ):

        if not Member.validate_name(name):
            raise EntityError('name')
        self.name = name
        
        if not Member.validate_ra(ra):
            raise EntityError('ra')
        self.ra = ra

        if not Member.validate_email_dev(email_dev):
            raise EntityError('email_dev')
        self.email_dev = email_dev

        if not Member.validate_email(email):
            raise EntityError('email')
        self.email = email
        
        if type(role) != ROLE:
            raise EntityError("role")
        self.role = role
        
        if type(stack) != STACK:
            raise EntityError("stack")
        self.stack = stack
        
        if not Member.validate_year(year):
            raise EntityError("year")
        self.year = year
        
        if not Member.validate_cellphone(cellphone):
            raise EntityError("cellphone")
        self.cellphone = cellphone
        
        if type(course) != COURSE:
            raise EntityError("course")
        self.course = course
        
        if type(hired_date) == int:
            if not 1577847601000 < hired_date:
                raise EntityError("hired_date")
            self.hired_date = hired_date
        else:
            raise EntityError("hired_date")
            
        
        if type(active) != ACTIVE:
            raise EntityError("active")
        self.active = active

        if not self.validate_user_id(user_id):
            raise EntityError("user_id")
        self.user_id = user_id
        
        if not self.validate_photo(photo):
            raise EntityError("photo")
        self.photo = photo
        
        if type(user_id) != str:
            raise EntityError("user_id")
            
        if deactivated_date is not None:
            if type(deactivated_date) != int:
                raise EntityError("deactivated_date")
            if deactivated_date < self.hired_date:
                raise EntityError("deactivated_date and hired_date") 
            if deactivated_date < 0:
                raise EntityError("deactivated_date")
            if not self.hired_date < deactivated_date:
                raise EntityError("deactivated_date")
            if active == ACTIVE.ACTIVE:
                raise EntityError("active")
        self.deactivated_date = deactivated_date

    @staticmethod
    def validate_year(year: int) -> bool:
        if year == None:
            return False
        
        if type(year) != int:
            return False

        return year > 0 and year <= 6
        
                
    @staticmethod
    def validate_ra(ra: str) -> bool:
        if ra == None:
            return False

        if type(ra) != str:
            raise EntityParameterTypeError('ra must be a string')

        return ra.isdecimal() and len(ra) == 8

    @staticmethod
    def validate_email_dev(email_dev) -> bool:
        if email_dev == None:
            return False
        if type(email_dev) != str:
            return False
        if email_dev[-18:] != ".devmaua@gmail.com":
            return False
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(re.fullmatch(regex, email_dev))

    @staticmethod
    def validate_name(name) -> bool:

        if name == None:
            return False
        
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
    def validate_email(email) -> bool:
        if email == None:
            return False
        if type(email) != str:
            return False
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return bool(re.fullmatch(regex, email))
    
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str: return False
        if len(user_id) != Member.USER_ID_LENGTH: return False
        return True
    
    @staticmethod
    def validate_role_admin(role: ROLE) -> bool:
        if role == None:
            return False
        if type(role) != ROLE:
            return False
        return (role == ROLE.DIRECTOR or role == ROLE.HEAD)
    
    @staticmethod
    def validate_active(active: ACTIVE) -> bool:
        if active == None:
            return False
        if type(active) != ACTIVE:
            return False
        return (active == ACTIVE.ACTIVE)
    
    @staticmethod
    def validate_photo(photo: str) -> bool:
        if photo is None: return True
        if type(photo) != str: return False
        return True
    
    def __repr__(self):
        return f"Member(name={self.name}, email_dev={self.email_dev}, email={self.email}, ra={self.ra}, role={self.role}, stack={self.stack}, year={self.year}, cellphone={self.cellphone}, course={self.course}, hired_date={self.hired_date}, deactivated_date={self.deactivated_date}, active={self.active}), user_id={self.user_id}"
    
    def __eq__(self, other):
        if not isinstance(other, Member):
            return False

        return self.name == other.name and self.email_dev == other.email_dev and self.email == other.email and self.ra == other.ra and self.role == other.role and self.stack == other.stack and self.year == other.year and self.cellphone == other.cellphone and self.course == other.course and self.hired_date == other.hired_date and self.deactivated_date == other.deactivated_date and self.active == other.active