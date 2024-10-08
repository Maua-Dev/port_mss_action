from typing import List
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK

class MemberViewModel:
    user_id: str
    name: str
    email_dev: str
    email: str
    role: ROLE
    stack: STACK
    year: int
    cellphone: str
    course: COURSE
    hired_date: int
    deactivated_date: int
    active: ACTIVE
    photo: str
    
    def __init__(self, member: Member):
        self.name = member.name
        self.email_dev = member.email_dev
        self.email = member.email
        self.user_id = member.user_id
        self.role = member.role
        self.stack = member.stack
        self.year = member.year
        self.cellphone = member.cellphone
        self.course = member.course
        self.hired_date = member.hired_date
        self.active = member.active
        self.deactivated_date = member.deactivated_date
        self.photo = member.photo
        
    def to_dict(self):
        return {
            'name' : self.name,
            'email_dev' : self.email_dev,
            'user_id' : self.user_id,
            'role' : self.role.value,
            'stack' : self.stack.value,
            'year' : self.year,
            'cellphone' : self.cellphone,
            'course' : self.course.value,
            'hired_date' : self.hired_date,
            'active' : self.active.value,
            'deactivated_date' : self.deactivated_date,
            'photo' : self.photo
        }

        
class UpdateMemberViewmodel:
    member:Member
    
    def __init__(self,member:Member):
        self.member =member
    
    def to_dict(self) -> dict:
        return {
            'member' : MemberViewModel(self.member).to_dict(),
            'message' : 'the member was updated'
        }