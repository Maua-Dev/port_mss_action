from src.modules.get_member_info.app.get_member_info_usecase import GetMemberInfoUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserNotAllowed
import pytest


class Test_GetMemberInfoUsecase:
    def test_get_member_info_usecase(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)

        # Usando o segundo membro ativo do mock - Joao Branco como requester
        members = usecase(requester_user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3')

        assert type(members) == list
        assert len(members) > 0
        assert type(members[0]) == Member

        # Validando se o vínculo de projetos funcionou para algum membro
        member_with_projects = next((m for m in members if m.name == 'Vitor Guirão MPNTM'), None)
        assert member_with_projects is not None
        assert hasattr(member_with_projects, 'project')
        assert isinstance(member_with_projects.project, list)
        assert len(member_with_projects.project) > 0

    def test_get_member_info_usecase_not_found_user_id(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)

        with pytest.raises(UnregisteredUser):
            usecase(requester_user_id='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')

    def test_get_member_info_usecase_freeze_user(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)

        # Luigi Televisão - FREEZE
        with pytest.raises(UserNotAllowed):
            usecase(requester_user_id='76h35dg4-h76v-1875-987hn-h67gfv45Gt4')

    def test_get_member_info_usecase_disconnected_user(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)

        # Marcos Pereira Neto - DISCONNECTED
        with pytest.raises(UserNotAllowed):
            usecase(requester_user_id='6574hgyt-785n-9134-18gn4-7gh5uvn36cG')

    def test_get_member_info_usecase_onhold_user(self):
        member_repo = MemberRepositoryMock()
        action_repo = ActionRepositoryMock()
        usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)

        # Carlinhos Miau - ON_HOLD
        with pytest.raises(UserNotAllowed):
            usecase(requester_user_id='3b07232f-4f65-42c6-b005-242550b8b8dc')