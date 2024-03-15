from typing import List
from src.shared.domain.entities.project import Project

class ProjectViewmodel:
    code: str
    name: str
    description: str
    po_user_id: str
    scrum_user_id: str
    start_date: int # milliseconds
    photos: List[str] = []

    def __init__(self, project: Project):
        self.code = project.code
        self.name = project.name
        self.description = project.description
        self.po_user_id = project.po_user_id
        self.scrum_user_id = project.scrum_user_id
        self.start_date = project.start_date
        self.photos = project.photos

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "po_user_id": self.po_user_id,
            "scrum_user_id": self.scrum_user_id,
            "start_date": self.start_date,
            "photos": self.photos
        }
    
class UpdateProjectViewmodel(ProjectViewmodel):
    update_project: ProjectViewmodel

    def __init__(self, update_project: Project):
        self.update_project = ProjectViewmodel(update_project)

    def to_dict(self):
        return{
            "project": self.update_project.to_dict(),
            "message": "the project was updated"
        }
