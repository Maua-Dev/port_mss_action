import pytest
from src.modules.create_action.app.create_action_usecase import CreateActionUsecase
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateActionUsecase:
    def test_create_action_usecase(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        lenBefore = len(repo.actions)
        
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=None, title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        
        new_action = usecase(action=action)
        assert len(repo.actions) == lenBefore + 1
        assert repo.actions[-1] == new_action == action
    
    def test_create_action_usecase_with_associated_members(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        lenActionBefore = len(repo.actions)
        lenAssociatedActionBefore = len(repo.associatedActions)
        
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=['21017310', '21010757'], title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        
        new_action = usecase(action=action)
        assert repo.actions[-1] == new_action == action
        assert len(repo.actions) == lenActionBefore + 1
        assert len(repo.associatedActions) == lenAssociatedActionBefore + 3
        assert repo.associatedActions[-2].member_ra == '21017310'
        assert repo.associatedActions[-1].member_ra == '21010757'
    
    def test_create_action_usecase_with_empty_list(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        lenActionBefore = len(repo.actions)
        
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id='82fc', associated_members_ra=[], title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        
        new_action = usecase(action=action)
        assert len(repo.actions) == lenActionBefore + 1
        assert repo.actions[-1] == new_action == action
    
    def test_create_action_usecase_duplicated_action_id(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        
        action = Action(owner_ra='17033730', start_time=1634526000000, action_id="u1e2", associated_members_ra=None, title='Teste', end_time=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tags=[ACTION_TYPE.CODE])
        
        with pytest.raises(DuplicatedItem):
            usecase(action=action)