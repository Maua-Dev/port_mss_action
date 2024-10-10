from typing import Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, PaginationAmountInvalid, UnregisteredUser, UserNotAllowed, UserIsNotFromAdmin
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE

class GetHistoryUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None, amount: Optional[int] = None, member_user_id: Optional[str] = None):

        if amount is None:
            amount = 20
        elif amount is not None and amount < 10:
            raise PaginationAmountInvalid()

        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()
        user = self.repo_member.get_member(user_id=user_id)
        
        if member_user_id is not None:
            if not self.repo_member.get_member(user_id=member_user_id):
                raise UnregisteredUser()
            
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()
        
        is_admin = Member.validate_role_admin(user.role)

        adjusted_amount = amount+1

        if is_admin and member_user_id is None:
            associated_actions = self.repo.get_associated_actions_by_user_id(user_id=user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=adjusted_amount)
        elif is_admin and member_user_id is not None:
            associated_actions = self.repo.get_associated_actions_by_user_id(user_id=member_user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=adjusted_amount)
        elif not is_admin and member_user_id is None:
            associated_actions = self.repo.get_associated_actions_by_user_id(user_id=user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=adjusted_amount)
        else:
            raise UserIsNotFromAdmin()
        
        actions_requested = associated_actions[:amount]
        
        last_ev = None
        if len(associated_actions) > amount:
            last_ev = (actions_requested[-1].action_id, actions_requested[-1].start_date)
        elif len(associated_actions) == amount:
            last_ev = None

        action_ids = [action.action_id for action in actions_requested]
        actions = self.repo.batch_get_action(action_ids=action_ids)
        actions = sorted(actions, key=lambda action: action.start_date, reverse= True)
        

        return actions, last_ev