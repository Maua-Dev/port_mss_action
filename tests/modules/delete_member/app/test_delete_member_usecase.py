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
        
        user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        
        member = usecase(user_id=user_id)
        assert type(member) == Member 
        assert len(repo.members) == len_before - 1
        assert member.user_id == user_id
        
    def test_delete_member_usecase_no_user_id_found(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        with pytest.raises(NoItemsFound):
            member = usecase(user_id='93bc6ada-gh46-7054-66ab-e17414c48ae3')
            
    def test_delete_member_usecase_invalid_code(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(user_id=123456789)
          