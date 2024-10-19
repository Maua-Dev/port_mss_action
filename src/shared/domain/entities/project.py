import abc
from datetime import datetime
from typing import List, Optional
from src.shared.helpers.errors.domain_errors import EntityError

class Project(abc.ABC):
    code: str
    name: str
    description: str
    po_user_id: str
    scrum_user_id: str
    start_date: int # milliseconds
    members_user_ids: List[str]
    photo: Optional[str] = None
    PROJECT_CODE_LENGTH = 2
    USER_ID_LENGTH = 36
    
    def __init__(self, code: str, name: str, description: str, po_user_id: str, scrum_user_id: str, start_date: int, members_user_ids: List[str], photo: Optional[str] = None):
        if not self.validate_project_code(code):
            raise EntityError("code")
        self.code = code
        
        if type(name) != str:
            raise EntityError("name")
        self.name = name
        
        if type(description) != str:
            raise EntityError("description")
        self.description = description
        
        if not self.validate_user_id(po_user_id):
            raise EntityError("po_user_id")
        self.po_user_id = po_user_id
        
        if not self.validate_user_id(scrum_user_id):
            raise EntityError("scrum_user_id")
        self.scrum_user_id = scrum_user_id
        
        if type(start_date) != int:
            raise EntityError("start_date")
        if start_date < 0:
            raise EntityError("start_date")
        if start_date > datetime.now().timestamp() * 1000:
            raise EntityError("start_date")
        self.start_date = start_date
        
        if photo is not None:
            if type(photo) != str:
                raise EntityError("photo")
            self.photo = photo
        
        if type(members_user_ids) != list:
            raise EntityError("members_user_ids")
        if len(members_user_ids) < 1:
            raise EntityError("members_user_ids")
        if po_user_id not in members_user_ids and scrum_user_id not in members_user_ids:
            raise EntityError("members_user_ids")
        if not all([self.validate_user_id(user_id) for user_id in members_user_ids]):
            raise EntityError("members_user_ids")
        self.members_user_ids = sorted(list(set(members_user_ids)))
        
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
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str: return False
        if len(user_id) != Project.USER_ID_LENGTH: return False
        return True
    
    def change_po_user_id(self, new_po_user_id: str):
        if not self.validate_user_id(new_po_user_id):
            raise EntityError("po_user_id")
        self.members_user_ids.remove(self.po_user_id)
        self.po_user_id = new_po_user_id
        self.members_user_ids.append(new_po_user_id)
        self.members_user_ids = sorted(list(set(self.members_user_ids)))

    def change_scrum_user_id(self, new_scrum_user_id: str):
        if not self.validate_user_id(new_scrum_user_id):
            raise EntityError("scrum_user_id")
        self.members_user_ids.remove(self.scrum_user_id)
        self.scrum_user_id = new_scrum_user_id
        self.members_user_ids.append(new_scrum_user_id)
        self.members_user_ids = sorted(list(set(self.members_user_ids)))
    
    def __repr__(self):
        return f"Project(code={self.code}, name={self.name}, description={self.description})"
    
    def __eq__(self, other):
        if type(other) != Project:
            return False
        return self.code == other.code and self.name == other.name and self.description == other.description
        
        