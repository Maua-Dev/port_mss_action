from typing import Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser
from src.shared.domain.entities.member import Member


class GetHistoryUsecase:
    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo
        self.repo_member = repo_member
        
    def __call__(self, user_id: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None, amount: Optional[int] = 20, member_user_id: Optional[str] = None):

        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()
        user = self.repo_member.get_member(user_id=user_id)
        
        if member_user_id is not None:
            if not self.repo_member.get_member(user_id=member_user_id):
                raise UnregisteredUser()
    
            
        
        is_admin = Member.validate_role_admin(user.role)
        if is_admin and member_user_id is None:
            associated_actions = self.repo.get_associated_actions_by_user_id(user_id=user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        elif is_admin and member_user_id is not None:
            associated_actions = self.repo.get_associated_actions_by_user_id(user_id=member_user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        elif not is_admin and member_user_id is None:
            associated_actions = self.repo.get_associated_actions_by_user_id(user_id=user_id, start=start, end=end, exclusive_start_key=exclusive_start_key, amount=amount)
        else:
            raise ForbiddenAction('user. Not allowed to access this resource.')
        
        action_ids = [action.action_id for action in associated_actions]
        actions = self.repo.batch_get_action(action_ids=action_ids)
        

        last_ev = (actions[-1].action_id, actions[-1].start_date) if len(actions) == amount else None
        return actions, last_ev