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
        
        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()
        
        
        if user.role not in [ROLE.DIRECTOR, ROLE.HEAD, ROLE.PO]:
            raise UserNotAllowed()
        
        action = self.repo_action.get_action(action_id)
        if not action:
            raise NoItemsFound('action')
        
        if not new_is_valid:
            self.repo_action.send_invalid_action_email(self.repo_user.get_member(action.user_id), action)
            for associated_member in action.associated_members_user_ids:
                self.repo_action.send_invalid_action_email(self.repo_user.get_member(associated_member), action)



        return self.repo_action.update_action(action_id=action_id, new_is_valid=new_is_valid)