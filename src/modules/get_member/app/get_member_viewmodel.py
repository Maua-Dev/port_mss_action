from typing import List
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK

class ProjectViewModel:
    code: str
    name: str
    description: str
    
    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
    
    def to_dict(self) -> dict:
        return {
            "code" : self.code,
            "name" : self.name,
            "description" : self.description
        }

class GetMemberViewmodel:
    name: str
    email: str
    ra: str
    role: ROLE
    stack: STACK
    year: int
    cellphone: str
    course: COURSE
    hired_date: int
    deactivated_date: int = None
    active: ACTIVE
    projects: List[Project]
    
    def __init__(self, member: Member):
        self.name = member.name
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
        
    def to_dict(self) -> dict:
        return {
            "member" : {
                "name" : self.name,
                "email" : self.email,
                "ra" : self.ra,
                "role" : self.role.value,
                "stack" : self.stack.value,
                "year" : self.year,
                "cellphone" : self.cellphone,
                "course" : self.course.value,
                "hired_date" : self.hired_date,
                "deactivated_date" : self.deactivated_date,
                "active" : self.active.value,
                "projects" : [ProjectViewModel(project).to_dict() for project in self.projects],
            },
            "message" : "the member was retrieved"
        }
