from typing import List
from src.shared.domain.entities.project import Project

class ProjectViewModel:
    code: str
    name: str
    description: str
    po_RA: str
    scrum_RA: str
    start_date: int
    photos: List[str] = None
    
    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
        self.po_RA = project.po_RA
        self.scrum_RA = project.scrum_RA
        self.start_date = project.start_date
        self.photos = project.photos if project.photos else []
        
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

class CreateProjectViewmodel:
    project: Project
    
    def __init__(self, project: Project):
        self.project = project
        
    def to_dict(self) -> dict:
        return {
            'project' : ProjectViewModel(self.project).to_dict(),
            'message' : 'the project was created'
        }