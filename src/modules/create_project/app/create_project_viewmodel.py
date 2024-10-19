from typing import List, Optional
from src.shared.domain.entities.project import Project

class ProjectViewModel:
    code: str
    name: str
    description: str
    po_user_id: str
    scrum_user_id: str
    start_date: int
    members_user_ids: List[str]
    photo: Optional[str] = None
    
    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
        self.po_user_id = project.po_user_id
        self.scrum_user_id = project.scrum_user_id
        self.start_date = project.start_date
        self.members_user_ids = project.members_user_ids
        self.photo = project.photo if project.photo else []
        
    def to_dict(self):
        return {
            'code' : self.code,
            'name' : self.name,
            'description' : self.description,
            'po_user_id' : self.po_user_id,
            'scrum_user_id' : self.scrum_user_id,
            'start_date' : self.start_date,
            'members_user_ids' : self.members_user_ids,
            'photo' : self.photo
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