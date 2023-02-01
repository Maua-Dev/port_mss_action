import pytest
from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetMemberUsecase:
    
    def test_get_member_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        
        member = usecase(ra='21017310')
        
        assert member == repo.members[0]
    
    def test_get_member_usecase_invalid_ra(self):
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        
        with pytest.raises(EntityError):
            member = usecase(ra='123')
    
    def test_get_member_usecase_no_member_found(self):
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        
        with pytest.raises(NoItemsFound):
            member = usecase(ra='12345678')