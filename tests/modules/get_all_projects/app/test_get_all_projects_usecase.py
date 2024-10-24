import pytest
from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase,ForbiddenAction, UserNotAllowed
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE


class Test_GetAllProjectsUsecase:
    def test_get_all_projects_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo, repo_member=repo_member)
        
        projects = usecase(repo_member.members[0].user_id)
        assert type(projects) == list
        assert len(projects) == 5
        assert type(projects[0]) == Project

    def test_get_all_projects_usecase_FREEZE_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo, repo_member=repo_member)
        user = repo_member.members[0]
        user.active= ACTIVE.FREEZE
        with pytest.raises(UserNotAllowed):
            usecase( user_id=user.user_id)
    
    def test_get_all_projects_usecase_DISCONNECTED_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase =GetAllProjectsUsecase(repo=repo, repo_member=repo_member)
        user = repo_member.members[0]
        user.active= ACTIVE.DISCONNECTED
        with pytest.raises(UserNotAllowed):
            usecase( user_id=user.user_id)

    def test_get_all_projects_usecase_no_start_and_end_date(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo, repo_member=repo_member)

        projects = usecase(repo_member.members[0].user_id)
        assert type(projects) == list
        assert len(projects) == 5
        assert type(projects[0]) == Project
        assert projects[0].hours_worked == 0