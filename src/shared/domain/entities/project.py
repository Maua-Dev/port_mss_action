import abc
from src.shared.helpers.errors.domain_errors import EntityError

class Project(abc.ABC):
    code: str
    name: str
    description: str
    PROJECT_CODE_LENGTH = 2
    
    def __init__(self, code: str, name: str, description: str):
        if not self.validate_project_code(code):
            raise EntityError("code")
        self.code = code
        
        if type(name) != str:
            raise EntityError("name")
        self.name = name
        
        if type(description) != str:
            raise EntityError("description")
        self.description = description
        
        
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
    
    def __repr__(self):
        return f"Project(code={self.code}, name={self.name}, description={self.description})"
    
    def __eq__(self, other):
        if type(other) != Project:
            return False
        return self.code == other.code and self.name == other.name and self.description == other.description
        
        