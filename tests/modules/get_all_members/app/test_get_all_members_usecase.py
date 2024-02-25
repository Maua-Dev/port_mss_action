from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest
class Test_GetAllMembersUseCase:
    def test_get_all_members_usecase(self):
        repo = MemberRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        
        members = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3")
        assert type(members) == list
        assert len(members) == 9
        assert all([type(member) == Member for member in members])


    def test_get_all_members_usecase_user_id_not_found(self):

        repo = MemberRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            members = usecase(user_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxdxxxxxx")
