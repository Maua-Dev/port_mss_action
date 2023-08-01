import pytest
from src.modules.get_history.app.get_history_usecase import GetHistoryUsecase
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetHistoryUsecase:
    def test_get_history_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo)
        actions, last_action_id = usecase(ra='17033730')

        assert all(type(action) is Action for action in actions)
        assert last_action_id == actions[-1].action_id
        
    def test_get_history_usecase_with_start_and_end(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo)
        actions, last_action_id = usecase(ra='17033730', start=1634526000000, end=1676476000000)

        assert all(type(action) is Action for action in actions)
        assert last_action_id == actions[-1].action_id
        
    def test_get_history_usecase_with_exclusive_start_key(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo)
        actions, last_action_id = usecase(ra='23017310', start=1634526000000, end=1676476000000, exclusive_start_key='87d4a661-0752-4ce2-9440-05e752e636fc')

        assert all(type(action) is Action for action in actions)
        assert last_action_id == actions[-1].action_id
        
    def test_get_history_usecase_with_amount(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo)
        actions, last_action_id = usecase(ra='17033730', amount=2)

        assert all(type(action) is Action for action in actions)
        assert last_action_id == actions[-1].action_id
        assert len(actions) == 2
            
    def test_get_history_usecase_no_items_found(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            usecase(ra='10039328')