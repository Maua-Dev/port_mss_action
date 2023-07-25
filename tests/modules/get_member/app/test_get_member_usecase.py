from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest

class Test_GetMemberUsecase:
    def test_get_member_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)

        member = usecase(ra='19017311')
        assert member == repo.members[5]
        assert type(member) == Member

    def test_get_member_usecase_not_found_ra(self):
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(ra='19010000')