from typing import List, Optional, Tuple
from src.shared.domain.entities.member import Member

from src.shared.domain.entities.project import Project

class ProjectViewModel:
    code: str
    name: str
    description: str
    po_RA: str
    scrum_RA: str
    start_date: int
    photos: List[str]

    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
        self.po_RA = project.po_RA
        self.scrum_RA = project.scrum_RA
        self.start_date = project.start_date
        self.photos = project.photos
        
    def to_dict(self):
        return {
            'code' : self.code,
            'name' : self.name,
            'description' : self.description,
            'po_RA' : self.po_RA,
            'scrum_RA' : self.scrum_RA,
            'start_date' : self.start_date,
            'photos' : self.photos
        }
        
class MemberViewModel:
    name: str
    email_dev: str
    email: str
    ra: str
    role: str
    stack: str
    year: int
    cellphone: str
    course: str
    hired_date: int
    deactivated_date: Optional[int] = None
    active: str
    projects: List[str]
    
    def __init__(self, member: Member):
        self.name = member.name
        self.email_dev = member.email_dev
        self.email = member.email
        self.ra = member.ra
        self.role = member.role.value
        self.stack = member.stack.value
        self.year = member.year
        self.cellphone = member.cellphone
        self.course = member.course.value
        self.hired_date = member.hired_date
        self.deactivated_date = member.deactivated_date
        self.active = member.active.value
        self.projects = member.projects
        
    def to_dict(self):
        return {
            'name' : self.name,
            'email_dev' : self.email_dev,
            'email' : self.email,
            'ra' : self.ra,
            'role' : self.role,
            'stack' : self.stack,
            'year' : self.year,
            'cellphone' : self.cellphone,
            'course' : self.course,
            'hired_date' : self.hired_date,
            'deactivated_date' : self.deactivated_date,
            'active' : self.active,
            'projects' : self.projects
        }

class GetProjectViewmodel:
    project: ProjectViewModel
    members: List[MemberViewModel]
    
    def __init__(self, project: Project, members: List[Member]):
        self.project = ProjectViewModel(project)
        self.members = [MemberViewModel(member) for member in members]
        
    def to_dict(self):
        return {
            'project' : self.project.to_dict(),
            'members' : [member.to_dict() for member in self.members]
        }

class GetAllProjectsViewmodel:
    projects_members: List[GetProjectViewmodel]
    
    def __init__(self, projects_members: List[Tuple[Project, List[Member]]]):	
        self.projects_members = [GetProjectViewmodel(project, members) for project, members in projects_members]
        
    def to_dict(self):
        return {
            'projects' : [project_member.to_dict() for project_member in self.projects_members],
            'message' : 'the projects were retrieved'
        }