import pytest
from src.modules.delete_project.app.delete_project_usecase import DeleteProjectUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_DeleteProjectUsecase:
    def test_delete_project_usecase(self):
        repo = ActionRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo)
        len_before = len(repo.projects)
        
        project = usecase(code='MF')
        assert len(repo.projects) == len_before - 1
        assert project.code == 'MF'
        
    def test_delete_project_usecase_no_items_found(self):
        repo = ActionRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            project = usecase(code='VT')
            
    def test_delete_project_usecase_invalid_code(self):
        repo = ActionRepositoryMock()
        usecase = DeleteProjectUsecase(repo=repo)
        with pytest.raises(EntityError):
            project = usecase(code='MauaFood')