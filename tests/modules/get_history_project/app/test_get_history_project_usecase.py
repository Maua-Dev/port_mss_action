import pytest
from src.modules.get_history_project.app.get_history_project_usecase import GetHistoryProjectUsecase
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, PaginationAmountInvalid, UserIsNotFromAdmin, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE


class Test_GetHistoryProjectUsecase:
    def test_get_history_project_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3',project_code= 'SF')

        assert all(type(action) is Action for action in actions)
        
    def test_get_history_project_usecase_with_start_and_end(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3', project_code= 'SF', start=1634526000000, end=1676476000000)

        assert all(type(action) is Action for action in actions)
        assert all(action.start_date >= 1634526000000 and action.start_date <= 1676476000000 for action in actions)
        
    def test_get_history_project_usecase_with_exclusive_start_key(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3', project_code= 'PT', start=1634526000000, end=1676476000000, exclusive_start_key={'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' : 1634526000000})
        print(actions, last_evaluated_key)

        assert all(type(action) is Action for action in actions)
        assert all(action.action_id != '87d4a661-0752-4ce2-9440-05e752e636fc' for action in actions)
        
    def test_get_history_project_usecase_with_amount(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3', project_code= 'SF', amount=10)

        assert all(type(action) is Action for action in actions)
        assert len(actions) == 4
            
    def test_get_history_project_usecase_unregistered_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        with pytest.raises(UnregisteredUser):
            usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
            actions, last_evaluated_key = usecase(user_id= 'adbc6ada-c0d1-7054-66ab-e17414c48ae3', project_code= 'PT')

    def test_get_history_project_usecase_forbidden_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        with pytest.raises(UserNotAllowed):
            usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
            actions, last_evaluated_key= usecase(user_id= repo_member.members[2].user_id,project_code=repo.actions[0].project_code)

    def test_get_history_project_usecase_another_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key= usecase(user_id= repo_member.members[0].user_id,project_code=repo.actions[0].project_code)

        assert all(type(action) is Action for action in actions)

    def test_get_history_project_usecase_amount_less_than_10(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        with pytest.raises(PaginationAmountInvalid):
            usecase = GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
            actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3',project_code='SF', amount=5)
    
    def test_get_history_project_usecase_DISCONNECTED_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase =GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        user = repo_member.members[0]
        action = repo.actions[0]
        user.active= ACTIVE.DISCONNECTED
        with pytest.raises(UserNotAllowed):
            actions, last_evaluated_key= usecase(user_id= user.user_id, project_code= action.project_code)
    
    def test_get_history_project_usecase_FREEZE_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase =GetHistoryProjectUsecase(repo=repo, repo_member=repo_member)
        user = repo_member.members[0]
        action = repo.actions[0]
        user.active= ACTIVE.FREEZE
        with pytest.raises(UserNotAllowed):
            actions, last_evaluated_key = usecase(user_id= user.user_id, project_code= action.project_code)