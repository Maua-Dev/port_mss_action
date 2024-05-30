import pytest
from src.modules.get_history.app.get_history_usecase import GetHistoryUsecase
from src.shared.domain.entities.action import Action
from src.shared.helpers.errors.controller_errors import WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnregisteredUser, PaginationAmountInvalid
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE


class Test_GetHistoryUsecase:
    def test_get_history_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3')

        assert all(type(action) is Action for action in actions)
        
    def test_get_history_usecase_with_start_and_end(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3', start=1634526000000, end=1676476000000)

        assert all(type(action) is Action for action in actions)
        assert all(action.start_date >= 1634526000000 and action.start_date <= 1676476000000 for action in actions)
        
    def test_get_history_usecase_with_exclusive_start_key(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '6f5g4h7J-876j-0098-123hb-hgb567fy4hb', start=1634526000000, end=1676476000000, exclusive_start_key={'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' : 1634526000000})
        print(actions, last_evaluated_key)

        assert all(type(action) is Action for action in actions)
        assert all(action.action_id != '87d4a661-0752-4ce2-9440-05e752e636fc' for action in actions)
        
    def test_get_history_usecase_with_amount(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3', amount=10)

        assert all(type(action) is Action for action in actions)
        assert len(actions) == 4
            
    def test_get_history_usecase_unregistered_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        with pytest.raises(UnregisteredUser):
            usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
            actions, last_evaluated_key = usecase(user_id= 'adbc6ada-c0d1-7054-66ab-e17414c48ae3')

    def test_get_history_usecase_forbidden_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        with pytest.raises(ForbiddenAction):
            usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
            actions, last_evaluated_key = usecase(user_id= repo_member.members[2].user_id, member_user_id=repo_member.members[0].user_id)

    def test_get_history_usecase_another_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
        actions, last_evaluated_key = usecase(user_id= repo_member.members[0].user_id, member_user_id=repo_member.members[2].user_id)

        assert all(type(action) is Action for action in actions)

    def test_get_history_usecase_amount_less_than_10(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        with pytest.raises(PaginationAmountInvalid):
            usecase = GetHistoryUsecase(repo=repo, repo_member=repo_member)
            actions, last_evaluated_key = usecase(user_id= '93bc6ada-c0d1-7054-66ab-e17414c48ae3', amount=5)
    
    def test_get_history_usecase_DISCONNECTED_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase =GetHistoryUsecase(repo=repo, repo_member=repo_member)
        user = repo_member.members[0]
        user.active= ACTIVE.DISCONNECTED
        with pytest.raises(ForbiddenAction):
            actions, last_evaluated_key = usecase(user_id= user.user_id)
    
    def test_get_history_usecase_FREEZE_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase =GetHistoryUsecase(repo=repo, repo_member=repo_member)
        user = repo_member.members[0]
        user.active= ACTIVE.FREEZE
        with pytest.raises(ForbiddenAction):
            actions, last_evaluated_key = usecase(user_id= user.user_id)