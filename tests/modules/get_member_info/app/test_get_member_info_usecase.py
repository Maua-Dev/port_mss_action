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

        members = usecase()

        assert type(members) == list
        assert len(members) > 0
        assert type(members[0]) == Member

        member_with_projects = next((m for m in members if m.name == 'Vitor Guirão MPNTM'), None)
        assert member_with_projects is not None
        assert hasattr(member_with_projects, 'project')
        assert isinstance(member_with_projects.project, list)
        assert len(member_with_projects.project) > 0
