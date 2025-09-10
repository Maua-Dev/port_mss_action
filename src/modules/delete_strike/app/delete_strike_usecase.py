from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserNotAllowed


class DeleteStrikeUseCase:
    def __init__(self, repo: IStrikeRepository, repo_member: IMemberRepository):
        self.repo_member = repo_member
        self.repo = repo

    def __call__(self, user_id: str, strike_id: str):

        if self.repo_member.get_member(user_id=user_id) is None:
            raise UnregisteredUser()

        if not Strike.validate_strike_id(strike_id):
            raise EntityError('strike_id')

        user = self.repo_member.get_member(user_id=user_id)

        if user.active != ACTIVE.ACTIVE:
            raise UserNotAllowed()

        strike = self.repo.get_strike(strike_id=strike_id)

        if strike is None:
            from src.shared.helpers.errors.usecase_errors import NoItemsFound
            raise NoItemsFound("No items found for strike_id")

        is_admin = user.validate_role_admin(user.role) and user.stack == STACK.RH

        if not is_admin and strike.owner_user_id != user.user_id:
            from src.shared.helpers.errors.usecase_errors import ForbiddenAction
            raise ForbiddenAction("type of user")

        strike = self.repo.delete_strike(strike_id=strike_id)

        return strike