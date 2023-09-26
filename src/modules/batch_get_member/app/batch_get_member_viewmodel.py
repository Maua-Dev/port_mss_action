from typing import List, Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK


class MemberViewModel:
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

    def to_dict(self):
        return {
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
            'active' : self.active.value
        }
        
class BatchGetMemberViewmodel:
    members: List[MemberViewModel]
    
    def __init__(self, members: List[Member]):
        self.members = [MemberViewModel(member) for member in members]
        
    def to_dict(self):
        return {
            'members' : [member.to_dict() for member in self.members],
            'message' : 'the members were retrieved'
        }