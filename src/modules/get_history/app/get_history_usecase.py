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
        if type(ra) is not str:
            raise WrongTypeParameter('ra', 'str', type(ra))
        
        if not Member.validate_ra(ra):
            raise EntityError('ra')
        
        if start:
            if type(start) is not int:
                raise WrongTypeParameter('start', 'int', type(start))
            if not 1000000000000 < start < 10000000000000:
                raise EntityError('start')
        if end:
            if type(end) is not int:
                raise WrongTypeParameter('end', 'int', type(end))
            if not 1000000000000 < end < 10000000000000:
                raise EntityError('end')
        if start and end:
            if start > end:
                raise EntityError('start')
        if exclusive_start_key:
            if not AssociatedAction.validate_action_id(exclusive_start_key):
                raise EntityError('exclusive_start_key')
                
            
        if type(amount) is not int:
            raise WrongTypeParameter('amount', 'int', type(amount))
        if amount < 1:
            raise EntityError('amount')
        
        associated_actions = self.repo.get_associated_actions_by_ra(ra=ra, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        
        if associated_actions == []:
            raise NoItemsFound('ra')
        
        action_ids = [action.action_id for action in associated_actions]
        actions = sorted(self.repo.batch_get_action(action_ids=action_ids), key=lambda action: action.start_date, reverse=True)
        
        return actions, associated_actions[-1].action_id