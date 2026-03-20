from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.strike_repository_interface import IStrikeRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser, UserNotAllowed


class DeleteStrikeUseCase:
    def __init__(self, repo: IStrikeRepository, repo_member: IMemberRepository):
        self.repo_member = repo_member
        self.repo = repo

    def __call__(self, user_id: str, strike_id: str):

        user = self.repo_member.get_member(user_id=user_id)

        if user is None:
            raise UnregisteredUser()
        
        if user.active != ACTIVE.ACTIVE or user.role not in [ROLE.DIRECTOR, ROLE.HEAD]:
            raise UserNotAllowed()

        strike = self.repo.find_by_id(strike_id=strike_id)

        if strike is None:
            from src.shared.helpers.errors.usecase_errors import NoItemsFound
            raise NoItemsFound("strike_id")

        is_admin = user.validate_role_admin(user.role)

        if not is_admin and strike.owner_user_id != user.user_id:
            from src.shared.helpers.errors.usecase_errors import ForbiddenAction
            raise ForbiddenAction("type of user")

        strike = self.repo.delete_strike(strike_id=strike_id)

        return strike