from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound

class CreateActionUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, action: Action) -> Action:
        
        if self.repo.get_action(action_id=action.action_id) is not None:
            raise DuplicatedItem('action_id')
        
        return self.repo.create_action(action)