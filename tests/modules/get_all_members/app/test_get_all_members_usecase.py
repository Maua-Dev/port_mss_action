from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetAllMembersUseCase:
    def test_get_all_members_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        
        members = usecase()
        assert type(members) == list
        assert len(members) == 8
        assert all([type(member) == Member for member in members])