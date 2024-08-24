import pytest
from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.shared.domain.enums.action_type_enum import ACTION_TYPE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE

class Test_UpdateActionUsecase:
    def test_update_action_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)

        action = usecase(action_id=repo.actions[0].action_id, user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3', new_start_date=1634526000000, new_story_id=100, new_associated_members_user_ids=['51ah5jaj-c9jm-1345-666ab-e12341c14a3'], new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)
        
        assert repo.actions[0] == action
        assert all(action.user_id in [action.user_id] for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert all(action.start_date == 1634526000000 for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert action.story_id == 100
        assert repo.actions[0].story_id == 100    

    def test_update_action_no_items_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)

        with pytest.raises(NoItemsFound):
            action = usecase(action_id='01538473-35ea-43c5-a823-f278c3fb42f3', user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3', new_start_date=1634526000000, new_story_id=100, new_associated_members_user_ids=['19017311'], new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)

    def test_update_action_usecase_another_member(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)

        action = usecase(action_id=repo.actions[0].action_id, user_id=repo_member.members[0].user_id, new_start_date=1634526000000, new_story_id=100, new_associated_members_user_ids=['51ah5jaj-c9jm-1345-666ab-e12341c14a3'], new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)
        
        assert repo.actions[0] == action
        assert all(action.user_id in [action.user_id] for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert all(action.start_date == 1634526000000 for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)

    def test_update_action_usecase_another_member_no_new_associated_members(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)

        action = usecase(action_id=repo.actions[0].action_id, user_id=repo_member.members[0].user_id, new_start_date=1634526000000, new_story_id=100, new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)
        
        assert repo.actions[0] == action
        assert all(action.user_id in [action.user_id] for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert all(action.start_date == 1634526000000 for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)

    def test_update_action_usecase_only_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)

        action = usecase(action_id=repo.actions[0].action_id, user_id=repo_member.members[0].user_id, new_start_date=1634526000000, new_story_id=100, new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)
        
        assert repo.actions[0] == action
        assert all(action.user_id in [action.user_id] for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert all(action.start_date == 1634526000000 for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)

    def test_update_action_usecase_another_member_forbidden_action(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)
        member = repo_member.members[2]
        member.active = ACTIVE.ACTIVE
        with pytest.raises(UserNotAllowed):
            action = usecase(action_id=repo.actions[0].action_id, user_id=member.user_id, new_start_date=1634526000000, new_story_id=100, new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)
    
    def test_update_action_user_is_FREEZE(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)
        member = repo_member.members[0]
        member.active = ACTIVE.FREEZE
        with pytest.raises(UserNotAllowed):
            action = usecase(action_id=repo.actions[0].action_id, user_id=member.user_id, new_start_date=1634526000000, new_story_id=100, new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)    
    
    def test_update_action_user_is_DISCONNECTED (self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)
        member = repo_member.members[0] 
        member.active = ACTIVE.DISCONNECTED
        with pytest.raises(UserNotAllowed):
            action = usecase(action_id=repo.actions[0].action_id, user_id=member.user_id, new_start_date=1634526000000, new_story_id=100, new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)    
    
    def test_update_action_admin(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)
        action = usecase(action_id=repo.actions[0].action_id, user_id=repo_member.members[0].user_id, new_start_date=1634526000000, new_story_id=100, new_associated_members_user_ids=[repo_member.members[0].user_id], new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)

        assert repo.actions[0] == action
        assert all(action.user_id in [action.user_id] for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert repo_member.members[0].user_id in action.associated_members_user_ids
    
    def test_update_action_zero(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo=repo, repo_member=repo_member)
        action = usecase(action_id=repo.actions[0].action_id, user_id=repo_member.members[0].user_id, new_start_date=1634526000000, new_story_id=0, new_associated_members_user_ids=[repo_member.members[0].user_id], new_title='Teste', new_end_date=1634536800000, new_project_code='MF', new_stack_tags=[STACK.BACKEND], new_action_type_tag=ACTION_TYPE.CODE)

        assert repo.actions[0] == action
        assert all(action.user_id in [action.user_id] for action in repo.associated_actions if action.action_id == repo.actions[0].action_id)
        assert action.story_id is None