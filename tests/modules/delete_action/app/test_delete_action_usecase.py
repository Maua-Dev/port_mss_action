import pytest
from src.modules.delete_action.app.delete_action_usecase import DeleteActionUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser


class Test_DeleteActionUsecase:
    def test_delete_action_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
        len_before = len(repo.actions)
        
        action_id=repo.actions[0].action_id
        
        action = usecase(action_id=action_id, user_id=repo_member.members[0].user_id)
        assert type(action) == Action 
        assert len(repo.actions) == len_before - 1
        assert action.action_id == action_id

    def test_delete_action_usecase_no_action_id_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
        with pytest.raises(NoItemsFound):
            action = usecase(action_id='711d1d26-f7c6-49e9-b0a0-84bdcfc21347', user_id=repo_member.members[0].user_id)

    def test_delete_action_usecase_invalid_acton_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
        with pytest.raises(EntityError):
            action = usecase(action_id=123456789, user_id=repo_member.members[0].user_id)

    def test_delete_action_usecase_no_user_id_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
        with pytest.raises(UnregisteredUser):
            action = usecase(action_id=repo.actions[0].action_id, user_id='93bc6ada-gh46-7054-66ab-e17414c48ae0')

    def test_delete_action_usecase_forbidden_user_with_member_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
        with pytest.raises(ForbiddenAction):
            action = usecase(action_id=repo.actions[0].action_id, user_id=repo_member.members[2].user_id, member_user_id=repo_member.members[1].user_id)

    def test_delete_action_usecase_admin_with_member_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = DeleteActionUsecase(repo_action=repo, repo_member=repo_member)
        len_before = len(repo.actions)
        
        action_id=repo.actions[0].action_id
        
        action = usecase(action_id=action_id, user_id=repo_member.members[0].user_id, member_user_id=repo_member.members[2].user_id)
        assert type(action) == Action 
        assert len(repo.actions) == len_before - 1
        assert action.action_id == action_id
