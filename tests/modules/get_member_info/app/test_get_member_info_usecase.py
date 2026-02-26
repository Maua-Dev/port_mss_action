from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
import pytest


class Test_GetMemberUsecase:
    def test_get_member_usecase(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetMemberUsecase(member_repo=member_repo, action_repo=action_repo, strike_repo=strike_repo)

        # Joao Branco - members[1]
        member = usecase(user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3')

        assert member.user_id == '51ah5jaj-c9jm-1345-666ab-e12341c14a3'
        assert type(member) == Member
        assert member.name == 'Joao Branco'

    def test_get_member_usecase_not_found_user_id(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetMemberUsecase(member_repo=member_repo, action_repo=action_repo, strike_repo=strike_repo)

        with pytest.raises(UnregisteredUser):
            usecase(user_id='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')

    def test_get_member_usecase_freeze_user(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetMemberUsecase(member_repo=member_repo, action_repo=action_repo, strike_repo=strike_repo)

        # Luigi Televisão - FREEZE
        with pytest.raises(UserNotAllowed):
            usecase(user_id='76h35dg4-h76v-1875-987hn-h67gfv45Gt4')

    def test_get_member_usecase_onhold_user(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        strike_repo = StrikeRepositoryMock()
        usecase = GetMemberUsecase(member_repo=member_repo, action_repo=action_repo, strike_repo=strike_repo)

        # Carlinhos Miau - ON_HOLD
        with pytest.raises(UserNotAllowed):
            usecase(user_id='3b07232f-4f65-42c6-b005-242550b8b8dc')