from src.shared.domain.entities.member import Member
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.course_enum import COURSE
from typing import List, Optional


class GetMemberInfoViewModel:
    name: str
    ra: str
    role: ROLE
    stack: STACK
    year: int
    course: COURSE
    project: List[str]
    hired_date: int
    photo: Optional[str]

    def __init__(self, member: Member):
        self.name = member.name
        self.ra = member.ra
        self.role = member.role
        self.stack = member.stack
        self.year = member.year
        self.course = member.course
        self.project = member.project if hasattr(member, 'project') else []
        self.hired_date = member.hired_date
        self.photo = member.photo

    def to_dict(self):
        return {
            'member_info': {
                'name': self.name,
                'ra': self.ra,
                'role': self.role.value,
                'stack': self.stack.value,
                'year': self.year,
                'course': self.course.value,
                'project': self.project,
                'hired_date': self.hired_date,
                'photo': self.photo
            },
            "message": "the member info was retrieved successfully"
        }