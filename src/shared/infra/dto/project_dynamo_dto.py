from typing import List, Optional

from src.shared.domain.entities.project import Project


class ProjectDynamoDTO:
    code: str
    name: str
    description: str
    po_user_id: str
    scrum_user_id: str
    start_date: int
    photo: Optional[str] = None
    members_user_ids: List[str] = []
    
    def __init__(self, code: str, name: str, description: str, po_user_id: str, scrum_user_id: str, start_date: int, photo: Optional[str] = None, members_user_ids: List[str] = []):
        self.code = code
        self.name = name
        self.description = description
        self.po_user_id = po_user_id
        self.scrum_user_id = scrum_user_id
        self.start_date = start_date
        self.photo = photo
        self.members_user_ids = members_user_ids
        
    @staticmethod
    def from_entity(project: Project) -> "ProjectDynamoDTO":
        return ProjectDynamoDTO(
            code=project.code,
            name=project.name,
            description=project.description,
            po_user_id=project.po_user_id,
            scrum_user_id=project.scrum_user_id,
            start_date=project.start_date,
            photo=project.photo,
            members_user_ids=project.members_user_ids
        )
        
    def to_dynamo(self) -> dict:       
        data = {
            "entity": "project",
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "po_user_id": self.po_user_id,
            "scrum_user_id": self.scrum_user_id,
            "start_date": self.start_date,
            "photo": self.photo,
            "members_user_ids": self.members_user_ids
        }
        
        return data
    
    @staticmethod
    def from_dynamo(data: dict) -> "ProjectDynamoDTO":
        return ProjectDynamoDTO(
            code=data["code"],
            name=data["name"],
            description=data["description"],
            po_user_id=data["po_user_id"],
            scrum_user_id=data["scrum_user_id"],
            start_date=data["start_date"],
            photo=data["photo"],
            members_user_ids=data["members_user_ids"]
        )
        
    def to_entity(self) -> Project:      
        return Project(
            code=self.code,
            name=self.name,
            description=self.description,
            po_user_id=self.po_user_id,
            scrum_user_id=self.scrum_user_id,
            start_date=int(self.start_date),
            photo=self.photo,
            members_user_ids=self.members_user_ids
        )
        
    def __repr__(self): 
        return f"ProjectDynamoDTO(code={self.code}, name={self.name}, description={self.description}, po_user_id={self.po_user_id}, scrum_user_id={self.scrum_user_id}, start_date={self.start_date}, photo={self.photo}, members_user_ids={self.members_user_ids})"

    def __eq__(self, other):
        if not isinstance(other, ProjectDynamoDTO):
            return False

        return self.code == other.code and self.name == other.name and self.description == other.description and self.po_user_id == other.po_user_id and self.scrum_user_id == other.scrum_user_id and self.start_date == other.start_date and self.photo == other.photo and self.members_user_ids == other.members_user_ids