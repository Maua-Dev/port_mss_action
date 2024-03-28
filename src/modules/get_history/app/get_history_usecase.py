from typing import Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser


class GetHistoryUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None, amount: Optional[int] = 20):

        if user_id is None:
            raise UnregisteredUser()
        
        associated_actions = self.repo.get_associated_actions_by_user_id(user_id=user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        
        action_ids = [action.action_id for action in associated_actions]
        actions = sorted(self.repo.batch_get_action(action_ids=action_ids), key=lambda action: action.start_date, reverse=True)
        
        last_ev = (actions[-1].action_id, actions[-1].start_date) if len(actions) > 0 else None
        return actions, last_ev