from typing import List
from src.shared.domain.entities.action import Action
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed, ForbiddenAction,UnregisteredUser
from src.shared.domain.enums.active_enum import ACTIVE

class UpdateActionValidationUsecase:
    def __init__(self, repo_action: IActionRepository, repo_member: IMemberRepository):
        self.repo_action = repo_action
        self.repo_user = repo_member
        
    def __call__(self, user_id: str, action_id: str, new_is_valid: bool) -> Action:
        
        user = self.repo_user.get_member(user_id)

        if user is None:
            raise UnregisteredUser()
        
        if user.role not in [ROLE.DIRECTOR, ROLE.HEAD, ROLE.PO]:
            raise UserNotAllowed()
        
        action = self.repo_action.get_action(action_id)
        if not action:
            raise NoItemsFound('action')
        
        if user.active != ACTIVE.ACTIVE:
            raise ForbiddenAction('active')

        return self.repo_action.update_action(action_id=action_id, new_is_valid=new_is_valid)