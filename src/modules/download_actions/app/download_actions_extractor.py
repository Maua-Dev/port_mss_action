from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class DownloadActionsExtractor:

    def __init__(self, repo: IActionRepository):
        self.repo_action = repo

    def __call__(self, project_code: str):
        
        if not Project.validate_project_code(project_code):
            raise EntityError('project_code')
        
        try:
            actions = self.repo_action.get_all_actions_and_associated_actions_by_project_code(project_code)
        except:
            raise NoItemsFound('actions')

        return actions