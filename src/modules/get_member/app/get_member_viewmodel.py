from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.course_enum import COURSE
from typing import List, Optional

class GetMemberViewModel:
    name: str
    email_dev: str
    email: str
    ra: str
    role: ROLE
    stack: STACK
    year: int
    cellphone: str
    course: COURSE
    hired_date: int
    deactivated_date: Optional[int] = None
    active: ACTIVE
    projects: Optional[List[str]] = None

    def __init__(self, member: Member):
        self.name = member.name
        self.email_dev = member.email_dev
        self.email = member.email
        self.ra = member.ra
        self.role = member.role
        self.stack = member.stack
        self.year = member.year
        self.cellphone = member.cellphone
        self.course = member.course
        self.hired_date = member.hired_date
        self.deactivated_date = member.deactivated_date
        self.active = member.active
        self.projects = member.projects

    def to_dict(self):
        return {
            'member':{
                'name' : self.name,
                'email_dev' : self.email_dev,
                'email' : self.email,
                'ra' : self.ra,
                'role' : self.role.value,
                'stack' : self.stack.value,
                'year' : self.year,
                'cellphone' : self.cellphone,
                'course' : self.course.value,
                'hired_date' : self.hired_date,
                'deactivated_date' : self.deactivated_date,
                'active' : self.active.value,
                'projects' : self.projects
            },
            "message" : "the member was retrieved"
        }