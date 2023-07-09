import abc
from datetime import datetime
from typing import List
from src.shared.helpers.errors.domain_errors import EntityError

class Project(abc.ABC):
    code: str
    name: str
    description: str
    po_RA: str
    scrum_RA: str
    start_date: int # milliseconds
    photos: List[str] = []
    PROJECT_CODE_LENGTH = 2
    
    def __init__(self, code: str, name: str, description: str, po_RA: str, scrum_RA: str, start_date: int, photos: List[str] = []):
        if not self.validate_project_code(code):
            raise EntityError("code")
        self.code = code
        
        if type(name) != str:
            raise EntityError("name")
        self.name = name
        
        if type(description) != str:
            raise EntityError("description")
        self.description = description
        
        if not self.validate_RA(po_RA):
            raise EntityError("po_RA")
        self.po_RA = po_RA
        
        if not self.validate_RA(scrum_RA):
            raise EntityError("scrum_RA")
        self.scrum_RA = scrum_RA
        
        if type(start_date) != int:
            raise EntityError("start_date")
        if start_date < 0:
            raise EntityError("start_date")
        if start_date > datetime.now().timestamp() * 1000:
            raise EntityError("start_date")
        self.start_date = start_date
        
        if type(photos) != list:
            raise EntityError("photos")
        for photo in photos:
            if type(photo) != str:
                raise EntityError("photos")
        self.photos = photos
        
        
    @staticmethod
    def validate_project_code(code: str) -> bool:
        if type(code) != str:
            return False
        if len(code) != Project.PROJECT_CODE_LENGTH:
            return False
        if not code.isupper():
            return False
        if not code.isalpha():
            return False
        return True
    
    @staticmethod
    def validate_RA(ra: str) -> bool:
        if type(ra) != str:
            return False
        if len(ra) != 8:
            return False
        if not ra.isdecimal():
            return False
        return True
    
    def __repr__(self):
        return f"Project(code={self.code}, name={self.name}, description={self.description})"
    
    def __eq__(self, other):
        if type(other) != Project:
            return False
        return self.code == other.code and self.name == other.name and self.description == other.description
        
        