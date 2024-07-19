import pytest
from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, UnregisteredUser
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_BatchGetMemberUsecase:
    def test_batch_get_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        
        members = usecase(user_id=repo.members[0].user_id, user_ids=[repo.members[0].user_id, repo.members[1].user_id])
        assert len(members) == 2
        assert all([type(member) == Member for member in members])
        assert members[0] == repo.members[0]
        assert members[1] == repo.members[1]
        
    def test_batch_get_member_usecase_with_duplicates(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        
        members = usecase(user_id=repo.members[0].user_id, user_ids=[repo.members[0].user_id, repo.members[0].user_id])
        assert len(members) == 1
        assert all([type(member) == Member for member in members])
        assert members[0] == repo.members[0]
        
    def test_batch_get_member_inactive_user(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        
        with pytest.raises(ForbiddenAction):
            usecase(user_id=repo.members[2].user_id, user_ids=[repo.members[0].user_id, repo.members[1].user_id])
            
    def test_batch_get_member_usecase_not_found_user_id(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)

        with pytest.raises(UnregisteredUser):
            usecase(user_id='5bah5aaj-c9jm-1345-666ab-e12341c14a3', user_ids=[repo.members[0].user_id, repo.members[1].user_id])