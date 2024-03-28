import pytest
from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetProjectUsecase:
    def test_get_project_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)

        project= usecase(code='MF')
        assert project.code == 'MF'
        assert type(project) == Project

    def test_get_project_usecase_no_items_found(self):
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(code='AA')