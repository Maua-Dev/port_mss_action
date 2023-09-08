from typing import Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetHistoryUsecase:
    def __init__(self, repo: IActionRepository):
        self.repo = repo
        
    def __call__(self, ra: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None, amount: Optional[int] = 20):
        
        associated_actions = self.repo.get_associated_actions_by_ra(ra=ra, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        
        action_ids = [action.action_id for action in associated_actions[0]]
        actions = sorted(self.repo.batch_get_action(action_ids=action_ids), key=lambda action: action.start_date, reverse=True)
        
        last_ev = (actions[-1].action_id, actions[-1].start_date) if len(actions) > 0 else None
        return actions, last_ev