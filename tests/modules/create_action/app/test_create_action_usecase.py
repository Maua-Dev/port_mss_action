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
        
        action = usecase(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_ra=[], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        
        assert len(repo.actions) == lenBefore + 1
        assert repo.actions[-1] == action
    
    def test_create_action_usecase_with_associated_members(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        lenActionBefore = len(repo.actions)
        lenAssociatedActionBefore = len(repo.associated_actions)
        
        action = usecase(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_ra=['21017310', '21010757'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        assert repo.actions[-1] == action
        assert len(repo.actions) == lenActionBefore + 1
        assert len(repo.associated_actions) == lenAssociatedActionBefore + 3
        assert repo.associated_actions[-2].member_ra == '21017310'
        assert repo.associated_actions[-1].member_ra == '21010757'
    
    def test_create_action_usecase_with_empty_list(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        lenActionBefore = len(repo.actions)
        
        action = usecase(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_ra=[], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)
        assert len(repo.actions) == lenActionBefore + 1
        assert repo.actions[-1] == action
        
    def test_create_action_usecase_ra_not_found(self):
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        lenActionBefore = len(repo.actions)
        
        with pytest.raises(NoItemsFound):
            action = usecase(owner_ra='17033730', start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_ra=['21017310', '21010757', '21010758'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE)