from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class DownloadActionsExtractor:

    def __init__(self, repo: IActionRepository):
        self.repo_action = repo

    def __call__(self):
        
        try:
            actions = self.repo_action.get_all_actions_and_associated_actions_by_project_code()
        except:
            raise NoItemsFound('actions')

        return actions