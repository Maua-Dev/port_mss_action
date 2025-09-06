from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserNotAllowed


class DeleteStrikeUseCase:
    def __init__(self, repo_strike: IStrikeRepository, repo: IMemberRepository):
        self.repo = repo
        self.repo_strike = repo_strike

    def __call__(self, user_id: str, strike_id: str):

        if self.repo.get_member(user_id=user_id) is None:
            raise UnregisteredUser()

        if not Strike.validate_strike_id(strike_id):
            raise EntityError('strike_id')

        user = self.repo.get_member(user_id=user_id)

        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()

        strike = self.repo_strike.get_strike(strike_id=strike_id)

        is_admin = user.validate_role_admin(user.role)

        if not is_admin or user.stack != STACK.RH:
            raise ForbiddenAction('This user can´t delete this strike. He is not the owner of the strike or an admin.')

        strike = self.repo_strike.delete_strike(strike_id=strike_id)

        if strike is None:
            raise EntityError('strike_id')

        return strike