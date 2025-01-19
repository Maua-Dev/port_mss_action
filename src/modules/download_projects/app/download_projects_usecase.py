from typing import Optional, Tuple
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, PaginationAmountInvalid, UnregisteredUser, UserNotAllowed, UserIsNotFromAdmin
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE

class DownloadProjectsUsecase:
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
        
        is_admin = Member.validate_role_admin(user.role) or Member.validate_role_external(user.role)


     
        actions = self.repo.get_projects_with_actions_and_associations()
        actions = sorted(actions, key=lambda action: action.start_date, reverse= True)
        
        download_link = self.repo.download_projects(actions)

        return actions