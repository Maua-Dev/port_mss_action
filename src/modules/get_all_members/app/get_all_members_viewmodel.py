from typing import List, Optional, Tuple
from src.shared.domain.entities.member import Member
from  src.shared.domain.enums.active_enum import ACTIVE
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
    project: Optional[List]
    year: int
    cellphone: str
    course: COURSE
    hired_date: int # milliseconds
    deactivated_date: Optional[int] = None # milliseconds
    active: ACTIVE
    user_id: str
    hours_worked: Optional[int] = None
    photo: Optional[str] = None 

    def __init__(self, member: Member):
        self.name = member.name
        self.email_dev = member.email_dev
        self.email = member.email
        self.ra = member.ra
        self.role = member.role
        self.stack = member.stack
        self.project = member.project
        self.year = member.year
        self.cellphone = member.cellphone
        self.course = member.course
        self.hired_date = member.hired_date
        self.deactivated_date = member.deactivated_date
        self.active = member.active
        self.user_id = member.user_id
        self.photo = member.photo
        self.hours_worked = member.hours_worked

    def to_dict(self):
        data = {
            'name': self.name,
            'email_dev': self.email_dev,
            'email': self.email,
            'ra': self.ra,
            'role': self.role.value,
            'stack': self.stack.value,
            'project': self.project,
            'year': self.year,
            'cellphone': self.cellphone,
            'course': self.course.value,
            'hired_date': self.hired_date,
            'deactivated_date': self.deactivated_date,
            'active': self.active.value,
            'user_id': self.user_id,
            'photo': self.photo
        }

  
        if self.hours_worked is not None:
            data['hours_worked'] = self.hours_worked
        
        return data

   
class GetMemberViewmodel:
    member: MemberViewModel

    def __init__(self, member: Member):
        self.member = MemberViewModel(member)

    def to_dict(self):
        return {
            'member' : self.member.to_dict()
        }
    
class GetAllMembersViewmodel:
    members: List[GetMemberViewmodel]

    def __init__(self, members: List[Tuple[Member]]):
        self.members = [GetMemberViewmodel(member) for member in members]

    def to_dict(self):
        return {
            'members' : [member.to_dict() for member in self.members],
            'message' : 'the members were retrieved'
        }