from typing import Optional
import uuid
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetHistoryUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, ra: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[str] = None, amount: Optional[int] = 20):
        
        associated_actions = self.repo.get_associated_actions_by_ra(ra=ra, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        
        if associated_actions == []:
            raise NoItemsFound('ra')
        
        action_ids = [action.action_id for action in associated_actions]
        actions = sorted(self.repo.batch_get_action(action_ids=action_ids), key=lambda action: action.start_date, reverse=True)
        
        return actions, associated_actions[-1].action_id