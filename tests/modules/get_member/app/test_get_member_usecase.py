from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser
import pytest

class Test_GetMemberUsecase:
    def test_get_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)

        member = usecase(user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3')
        assert member == repo.members[1]
        assert type(member) == Member

    def test_get_member_usecase_not_found_user_id(self):
        repo = MemberRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)

        with pytest.raises(UnregisteredUser):
            usecase(user_id='5bah5aaj-c9jm-1345-666ab-e12341c14a3')
        
    def test_get_member_usecase_inactive_user(self):
        repo = MemberRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(user_id='76h35dg4-h76v-1875-987hn-h67gfv45Gt4')
            
    def test_get_member_usecase_onhold_user(self):
        repo = MemberRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(user_id='3b07232f-4f65-42c6-b005-242550b8b8dc')