from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_ActionRepositoryMock:
    def test_get_member(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra=repo.members[1].ra)
        
        assert type(member) == Member
        assert member == repo.members[1]
        
    def test_get_member_not_found(self):
        repo = ActionRepositoryMock()
        member = repo.get_member(ra="21010101")
        
        assert member is None