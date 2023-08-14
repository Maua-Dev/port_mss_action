from typing import List
from src.shared.domain.entities.project import Project

class ProjectViewModel:
    code: str
    name: str
    description: str
    po_RA: str
    scrum_RA: str
    start_date: int
    members: List[str]
    photos: List[str]

    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
        self.po_RA = project.po_RA
        self.scrum_RA = project.scrum_RA
        self.start_date = project.start_date
        self.members = project.members
        self.photos = project.photos

    def to_dict(self):
        return {
            'code' : self.code,
            'name' : self.name,
            'description' : self.description,
            'po_RA' : self.po_RA,
            'scrum_RA' : self.scrum_RA,
            'start_date' : self.start_date,
            'members' : self.members,
            'photos' : self.photos
        }

class DeleteProjectViewModel:
    project: ProjectViewModel
    
    def __init__(self, project: Project):
        self.project = ProjectViewModel(project)
        
    def to_dict(self):
        return {
            'project' : self.project.to_dict(),
            'message' : 'the project was deleted'
        }