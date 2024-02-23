from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

class Test_GetAllMembersUseCase:
    def test_get_all_members_usecase(self):
        repo = MemberRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        
        members = usecase()
        assert type(members) == list
        assert len(members) == 9
        assert all([type(member) == Member for member in members])