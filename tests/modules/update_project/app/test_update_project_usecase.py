import pytest
from src.modules.update_project.app.update_project_usecase import UpdateProjectUsecase
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class TestUpdateProjectUsecase:

    def test_update_project(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        update_project = usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "21017311", new_scrum_user_id = "21010755", new_photos = ["foto1", "foto2"])

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_user_id == update_project.po_user_id
        assert repo.projects[1].scrum_user_id == update_project.scrum_user_id
        assert repo.projects[1].photos == update_project.photos


    def test_update_project_one_parameter(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        update_project = usecase(code = "PT", new_name = "Novo nome", new_description = "É um site", new_po_user_id = "22011020", new_scrum_user_id = "21010757", new_photos = ["https://i.imgur.com/gHoRKJU.png"])

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_user_id == update_project.po_user_id
        assert repo.projects[1].scrum_user_id == update_project.scrum_user_id
        assert repo.projects[1].photos == update_project.photos

    def test_update_project_not_found(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(code = "RR", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "21017311", new_scrum_user_id = "21010755", new_photos = ["foto1", "foto2"])

    def test_update_project_only_scrumRA(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        update_project = usecase(code = "PT", new_name = None, new_description = None, new_po_user_id = None, new_scrum_user_id = "21010757", new_photos = None)

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_user_id == update_project.po_user_id
        assert repo.projects[1].scrum_user_id == update_project.scrum_user_id
        assert repo.projects[1].photos == update_project.photos