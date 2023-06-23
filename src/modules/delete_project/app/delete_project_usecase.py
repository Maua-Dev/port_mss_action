from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteProjectUsecase:
    def __init__(self, repo:IActionRepository):
        self.repo = repo
    
    def __call__(self, code: str):
        if not Project.validate_project_code(code):
            raise EntityError('code')
        
        project = self.repo.delete_project(code=code)
        
        if project is None:
            raise NoItemsFound('project')
        
        return project