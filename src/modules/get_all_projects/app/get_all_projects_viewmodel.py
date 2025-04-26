from typing import List, Optional, Tuple
from src.shared.domain.entities.member import Member

from src.shared.domain.entities.project import Project

class ProjectViewModel:
    code: str
    name: str
    description: str
    po_user_id: str
    scrum_user_id: str
    start_date: int
    members_user_ids: List[str]
    photos: List[str] = None
    
    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
        self.po_user_id = project.po_user_id
        self.scrum_user_id = project.scrum_user_id
        self.start_date = project.start_date
        self.members_user_ids = project.members_user_ids
        self.photos = project.photos if project.photos else []
        
    def to_dict(self):
        return {
            'code' : self.code,
            'name' : self.name,
            'description' : self.description,
            'po_user_id' : self.po_user_id,
            'scrum_user_id' : self.scrum_user_id,
            'start_date' : self.start_date,
            'members_user_ids' : self.members_user_ids,
            'photos' : self.photos
        }
        
class GetProjectViewmodel:
    project: ProjectViewModel
    
    def __init__(self, project: Project):
        self.project = ProjectViewModel(project)
        
    def to_dict(self):
        return {
            'project' : self.project.to_dict()
        }

class GetAllProjectsViewmodel:
    projects: List[GetProjectViewmodel]
    
    def __init__(self, projects: List[Tuple[Project]]):	
        self.projects = [GetProjectViewmodel(project) for project in projects]
        
    def to_dict(self):
        return {
            'projects' : [project.to_dict() for project in self.projects],
            'message' : 'the projects were retrieved'
        }