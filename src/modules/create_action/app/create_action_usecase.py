from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound

class CreateActionUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, action: Action) -> Action:
        
        if self.repo.get_action(action_id=action.action_id) is not None:
            raise DuplicatedItem('action_id')
        
        if self.repo.get_member(ra=action.owner_ra) is None:
            raise NoItemsFound('owner_ra')
        
        if action.associated_members_ra is not None:
            members = self.repo.get_members(ras=action.associated_members_ra)
            if len(members) != len(action.associated_members_ra):
                raise NoItemsFound('associated_members_ra')
        
        return self.repo.create_action(action)