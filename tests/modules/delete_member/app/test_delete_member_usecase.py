import pytest
from src.modules.delete_member.app.delete_member_usecase import DeleteMemberUseCase
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteMemberUserCase:
    def test_delete_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        len_before = len(repo.members)
        
        member = usecase(ra='21017310')
        assert type(member) == Member 
        assert len(repo.members) == len_before - 1
        assert member.ra == '21017310'
        
    def test_delete_member_usecase_no_ra_found(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        with pytest.raises(NoItemsFound):
            member = usecase(ra='21017311')
            
    def test_delete_member_usecase_invalid_code(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(ra=123456789)
          