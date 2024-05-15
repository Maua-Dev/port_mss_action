import pytest
from src.modules.update_action_validation.app.update_action_validation_usecase import UpdateActionValidationUsecase
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UserNotAllowed, UnregisteredUser
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE

class TestUpdateActionValidationUsecase:
    def test_update_action_validation_usecase(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionValidationUsecase(repo_action, repo_member)
        action = repo_action.actions[0]
        member = repo_member.members[0]
        new_validation = usecase(user_id=member.user_id, action_id= action.action_id, new_is_valid=False)
        
        assert new_validation.action_id == action.action_id
        assert new_validation.is_valid == False

    def test_update_action_validation_usecase_no_action_found(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionValidationUsecase(repo_action, repo_member)
        member = repo_member.members[0]
        with pytest.raises(NoItemsFound):
            usecase(user_id=member.user_id, action_id= 'invalid_id', new_is_valid=False)

    def test_update_action_validation_usecase_unregistered_user(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        action = repo_action.actions[0]
        usecase = UpdateActionValidationUsecase(repo_action, repo_member)
        with pytest.raises(UnregisteredUser):
            usecase(user_id='invalid_id', action_id=action.action_id , new_is_valid=False)

    def test_update_action_validation_usecase_user_not_allowed(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        action = repo_action.actions[0]
        member = repo_member.members[2]
        usecase = UpdateActionValidationUsecase(repo_action, repo_member)
        with pytest.raises(UserNotAllowed):
            usecase(user_id=member.user_id, action_id=action.action_id , new_is_valid=False)
    
    def test_update_action_validation_usecase_user_is_FREEZE(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        action = repo_action.actions[0]
        member = repo_member.members[0]
        member.active = ACTIVE.FREEZE
        usecase = UpdateActionValidationUsecase(repo_action, repo_member)
        with pytest.raises(UserNotAllowed):
            usecase(user_id=member.user_id, action_id=action.action_id , new_is_valid=False)
            
    def test_update_action_validation_usecase_user_is_DISCONNECTED(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        action = repo_action.actions[0]
        member = repo_member.members[0]
        member.active = ACTIVE.DISCONNECTED
        usecase = UpdateActionValidationUsecase(repo_action, repo_member)
        with pytest.raises(UserNotAllowed):
            usecase(user_id=member.user_id, action_id=action.action_id , new_is_valid=False)
            