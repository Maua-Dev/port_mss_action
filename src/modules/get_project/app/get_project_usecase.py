from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetProjectUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, code: str):
        
        project = self.repo.get_project(code=code)
        if project is None:
            raise NoItemsFound('code')
        
        return project