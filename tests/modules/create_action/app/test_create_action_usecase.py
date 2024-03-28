import pytest
from src.modules.create_action.app.create_action_usecase import CreateActionUsecase
from src.shared.domain.entities.action import Action
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_CreateActionUsecase:
    def test_create_action_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateActionUsecase(repo=repo, repo_member=repo_member)
        lenBefore = len(repo.actions)
        
        action = usecase(start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_user_ids=[], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE, user_id="75648hbr-184n-1985-91han-7ghn4HgF182", is_valid=True)
        
        assert len(repo.actions) == lenBefore + 1
        assert repo.actions[-1] == action
    
    def test_create_action_usecase_with_associated_members(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateActionUsecase(repo=repo, repo_member=repo_member)
        lenActionBefore = len(repo.actions)
        lenAssociatedActionBefore = len(repo.associated_actions)
        
        action = usecase(start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_user_ids=['9183jBnh-997H-1010-10god-914gHy46tBh', '7465hvnb-143g-1675-86HnG-75hgnFbcg36'], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE, user_id="75648hbr-184n-1985-91han-7ghn4HgF182", is_valid=True)
        assert repo.actions[-1] == action
        assert len(repo.actions) == lenActionBefore + 1
        assert len(repo.associated_actions) == lenAssociatedActionBefore + 3
        assert repo.associated_actions[-2].user_id == '9183jBnh-997H-1010-10god-914gHy46tBh'
        assert repo.associated_actions[-1].user_id == '7465hvnb-143g-1675-86HnG-75hgnFbcg36'
    
    def test_create_action_usecase_with_empty_list(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateActionUsecase(repo=repo, repo_member=repo_member)
        lenActionBefore = len(repo.actions)
        
        action = usecase(start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_user_ids=[], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE, user_id="75648hbr-184n-1985-91han-7ghn4HgF182", is_valid=True)
        assert len(repo.actions) == lenActionBefore + 1
        assert repo.actions[-1] == action
        
    def test_create_action_usecase_unregistered_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = CreateActionUsecase(repo=repo, repo_member=repo_member)
        lenActionBefore = len(repo.actions)
        
        with pytest.raises(UnregisteredUser):
            action = usecase(start_date=1634526000000, duration=2*60*60*1000, story_id=100, associated_members_user_ids=['9183jBnh-997H-1010-10god-914gHy46tBh', '7465hvnb-143g-1675-86HnG-75hgnFbcg36', "pd8njBnh-997H-1010-10god-914gHy46tBh"], title='Teste', end_date=1634536800000, project_code='MF', stack_tags=[STACK.BACKEND], action_type_tag=ACTION_TYPE.CODE, user_id="75648hbr-184n-1985-91han-7ghn4HgF182", is_valid=True)