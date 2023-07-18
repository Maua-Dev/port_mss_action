from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetProjectUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, code: str):
        
        if type(code) is not str:
                raise WrongTypeParameter('code', 'str', type(code))
            
        if not Project.validate_project_code(code):
                raise EntityError('code')
            
        project = self.repo.get_project(code=code)
        if project is None:
            raise NoItemsFound('code')
        
        tup = project, self.repo.get_members_by_project(code=code)
        
        return tup