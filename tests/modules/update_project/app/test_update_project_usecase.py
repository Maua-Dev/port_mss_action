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
        update_project = usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_RA = "21017311", new_scrum_RA = "21010755", new_photos = ["foto1", "foto2"])

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_RA == update_project.po_RA
        assert repo.projects[1].scrum_RA == update_project.scrum_RA
        assert repo.projects[1].photos == update_project.photos


    def test_update_project_one_parameter(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        update_project = usecase(code = "PT", new_name = "Novo nome", new_description = "É um site", new_po_RA = "22011020", new_scrum_RA = "21010757", new_photos = ["https://i.imgur.com/gHoRKJU.png"])

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_RA == update_project.po_RA
        assert repo.projects[1].scrum_RA == update_project.scrum_RA
        assert repo.projects[1].photos == update_project.photos


    def test_update_project_invalid_code(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)

        with pytest.raises(EntityError):
            usecase(code = 555, new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_RA = "21017311", new_scrum_RA = "21010755", new_photos = ["foto1", "foto2"])

    def test_update_project_invalid_name(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)

        with pytest.raises(EntityError):
            usecase(code = "PT", new_name = 555, new_description = "Descrição do projeto teste", new_po_RA = "21017311", new_scrum_RA = "21010755", new_photos = ["foto1", "foto2"])

    def test_update_project_not_found(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(code = "RR", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_RA = "21017311", new_scrum_RA = "21010755", new_photos = ["foto1", "foto2"])