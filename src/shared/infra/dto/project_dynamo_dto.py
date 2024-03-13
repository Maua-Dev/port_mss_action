from typing import List, Optional

from src.shared.domain.entities.project import Project


class ProjectDynamoDTO:
    code: str
    name: str
    description: str
    po_RA: str
    scrum_RA: str
    start_date: int
    members: List[str]
    photos: Optional[List[str]] = []
    members_user_ids: List[str] = []
    
    def __init__(self, code: str, name: str, description: str, po_RA: str, scrum_RA: str, start_date: int, members: List[str], photos: Optional[List[str]] = [], members_user_ids: List[str] = []):
        self.code = code
        self.name = name
        self.description = description
        self.po_RA = po_RA
        self.scrum_RA = scrum_RA
        self.start_date = start_date
        self.members = members
        self.photos = photos
        self.members_user_ids = members_user_ids
        
    @staticmethod
    def from_entity(project: Project) -> "ProjectDynamoDTO":
        return ProjectDynamoDTO(
            code=project.code,
            name=project.name,
            description=project.description,
            po_RA=project.po_RA,
            scrum_RA=project.scrum_RA,
            start_date=project.start_date,
            members=project.members,
            photos=project.photos,
            members_user_ids=project.members_user_ids
        )
        
    def to_dynamo(self) -> dict:       
        data = {
            "entity": "project",
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "po_RA": self.po_RA,
            "scrum_RA": self.scrum_RA,
            "start_date": self.start_date,
            "members": self.members,
            "photos": self.photos if self.photos else [],
            "members_user_ids": self.members_user_ids
        }
        
        return data
    
    @staticmethod
    def from_dynamo(data: dict) -> "ProjectDynamoDTO":
        return ProjectDynamoDTO(
            code=data["code"],
            name=data["name"],
            description=data["description"],
            po_RA=data["po_RA"],
            scrum_RA=data["scrum_RA"],
            start_date=data["start_date"],
            members=data["members"],
            photos=data["photos"] if "photos" in data else [],
            members_user_ids=data["members_user_ids"] if "members_user_ids" in data else []
        )
        
    def to_entity(self) -> Project:      
        return Project(
            code=self.code,
            name=self.name,
            description=self.description,
            po_RA=self.po_RA,
            scrum_RA=self.scrum_RA,
            start_date=int(self.start_date),
            members=self.members,
            photos=self.photos,
            members_user_ids=self.members_user_ids
        )
        
    def __repr__(self): 
        return f"ProjectDynamoDTO(code={self.code}, name={self.name}, description={self.description}, po_RA={self.po_RA}, scrum_RA={self.scrum_RA}, start_date={self.start_date}, members={self.members}, photos={self.photos}, members_user_ids={self.members_user_ids})"

    def __eq__(self, other):
        if not isinstance(other, ProjectDynamoDTO):
            return False

        return self.code == other.code and self.name == other.name and self.description == other.description and self.po_RA == other.po_RA and self.scrum_RA == other.scrum_RA and self.start_date == other.start_date and self.members == other.members and self.photos == other.photos and self.members_user_ids == other.members_user_ids