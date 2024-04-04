import pytest
from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.usecase_errors import NoItemsFound, UnregisteredUser
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetProjectUsecase:
    def test_get_project_usecase(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)

        project= usecase(code='MF', user_id=repo_member.members[0].user_id)
        assert project.code == 'MF'
        assert type(project) == Project

    def test_get_project_usecase_no_items_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)

        with pytest.raises(NoItemsFound):
            usecase(code='AA', user_id=repo_member.members[0].user_id)
    
    def test_get_project_usecase_no_user_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)

        with pytest.raises(UnregisteredUser):
            usecase(code='AA', user_id='1234')