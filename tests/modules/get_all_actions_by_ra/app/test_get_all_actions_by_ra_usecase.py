import pytest
from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_usecase import GetAllActionsByRaUsecase
from src.shared.domain.entities.associated_action import AssociatedAction
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetAllActionsByRaUsecase:
    def test_get_all_actions_by_ra_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo=repo)
        actions = usecase(ra='21010757')
        assert type(actions) == list
        assert all(type(action) == AssociatedAction for action in actions)
        
    def test_get_all_actions_by_ra_usecase_member_not_found(self):
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            usecase(ra='00000000')
            
    def test_get_all_actions_by_ra_usecase_invalid_ra(self):
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo=repo)
        with pytest.raises(EntityError):
            usecase(ra='123')