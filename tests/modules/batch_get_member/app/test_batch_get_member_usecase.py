from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.shared.domain.entities.member import Member
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_BatchGetMemberUsecase:
    def test_batch_get_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        
        members = usecase(user_ids=[repo.members[0].user_id, repo.members[1].user_id])
        assert len(members) == 2
        assert all([type(member) == Member for member in members])
        assert members[0] == repo.members[0]
        assert members[1] == repo.members[1]
        
    def test_batch_get_member_usecase_with_duplicates(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        
        members = usecase(user_ids=[repo.members[0].user_id, repo.members[0].user_id])
        assert len(members) == 1
        assert all([type(member) == Member for member in members])
        assert members[0] == repo.members[0]