import pytest
from src.modules.delete_member.app.delete_member_usecase import DeleteMemberUseCase
from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_DeleteMemberUseCase:
    def test_delete_member_usecase(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        len_before = len(repo.members)
        
        user_id=repo.members[0].user_id
        
        member = usecase(user_id=user_id)
        assert type(member) == Member 
        assert len(repo.members) == len_before - 1
        assert member.user_id == user_id
        
    def test_delete_member_usecase_no_user_id_found(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(user_id='93bc6ada-gh46-7054-66ab-e17414c48ae3')
            
    def test_delete_member_usecase_invalid_code(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        with pytest.raises(EntityError):
            member = usecase(user_id=123456789)
    
    def test_delete_member_usecase_with_member_user_id(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        len_before = len(repo.members)
        
        user_id=repo.members[0].user_id
        member_user_id=repo.members[1].user_id
        
        member = usecase(user_id=user_id, member_user_id=member_user_id)
        assert type(member) == Member 
        assert len(repo.members) == len_before - 1
        assert member.user_id == member_user_id
    
    def test_delete_member_usecase_forbidden_user_with_member_user_id(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        len_before = len(repo.members)
        
        user_id=repo.members[2].user_id
        member_user_id=repo.members[1].user_id


        with pytest.raises(ForbiddenAction):
            member = usecase(user_id=user_id, member_user_id=member_user_id)
    
    def test_delete_member_usecase_forbidden_user_with_member_user_id(self):
        repo = MemberRepositoryMock()
        usecase = DeleteMemberUseCase(repo=repo)
        len_before = len(repo.members)
        
        user_id=repo.members[2].user_id
        member_user_id=repo.members[1].user_id


        with pytest.raises(ForbiddenAction):
            member = usecase(user_id=user_id, member_user_id=member_user_id)
          