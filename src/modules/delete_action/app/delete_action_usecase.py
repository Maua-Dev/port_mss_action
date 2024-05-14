from src.shared.domain.entities.action import Action
from src.shared.domain.repositories.action_repository_interface import IActionRepository
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser, ForbiddenAction
from src.shared.helpers.errors.domain_errors import EntityError
from typing import Optional


class DeleteActionUsecase:
    def __init__(self, repo_action: IActionRepository, repo_member: IMemberRepository):
        self.action_repository = repo_action
        self.member_repository = repo_member

    def __call__(self, action_id: str, user_id: str, member_user_id: Optional[str] = None) -> Action:
        if self.member_repository.get_member(user_id=user_id) is None:
            raise UnregisteredUser()
        
        if not Action.validate_action_id(action_id):
            raise EntityError('action_id')

        user = self.member_repository.get_member(user_id=user_id)

        action = self.action_repository.get_action(action_id=action_id) 

        is_admin = user.validate_role_admin(user.role)
        if is_admin == False and user_id != action.user_id:
            raise ForbiddenAction('This user can´t update this action. He is not the owner of the action or an admin.')

        if is_admin and member_user_id is None:
            action = self.action_repository.delete_action(action_id=action_id)
        elif is_admin and member_user_id is not None:
            action = self.action_repository.delete_action(action_id=action_id)
        elif not is_admin and member_user_id is None:
            action = self.action_repository.delete_action(action_id=action_id)

        if action is None:
            raise NoItemsFound('action_id')
        
        return action