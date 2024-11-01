from typing import Optional
from src.shared.domain.entities.project import Project
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, PaginationAmountInvalid, UnregisteredUser, UserNotAllowed, UserIsNotFromAdmin
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.domain.enums.active_enum import ACTIVE

class GetHistoryProjectUsecase:

    def __init__(self, repo: IActionRepository, repo_member: IMemberRepository):
        self.repo = repo 
        self.repo_member = repo_member 
    
    def __call__(self, user_id: str, code: str, start: Optional[int] = None, end: Optional[int] = None, exclusive_start_key: Optional[dict] = None, amount: Optional[int] = None, member_user_id: Optional[str] = None):
    
        if not Project.validate_project_code(code):
            raise EntityError('code')
            
        project = self.repo.get_project(code=code)
        if project is None:
            raise NoItemsFound('code')

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
        
        actions = self.repo.get_all_actions_by_project_code(code=code)
        actions = sorted(actions, key=lambda action: action.start_date, reverse= True)

        last_ev = None
        if len(actions) > amount:
            last_ev = (actions[-1].action_id, actions[-1].start_date)
        elif len(actions) == amount:
            last_ev = None

        

        return actions, last_ev
