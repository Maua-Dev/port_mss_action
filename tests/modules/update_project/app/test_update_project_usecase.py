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
        update_project = usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_scrum_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_photos = ["foto1", "foto2"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"])

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_user_id == update_project.po_user_id
        assert repo.projects[1].scrum_user_id == update_project.scrum_user_id
        assert repo.projects[1].photos == update_project.photos


    def test_update_project_one_parameter(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        update_project = usecase(code = "PT", new_name = "Novo nome", new_description = "É um site", new_po_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_scrum_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_photos = ["https://i.imgur.com/gHoRKJU.png"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"])

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
            usecase(code = "RR", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "6574hgyt-785n-9134-18gn4-7gh5uvn36cG", new_scrum_user_id = "7gh5yf5H-857H-1234-75hng-94832hvng1s", new_photos = ["foto1", "foto2"])

    def test_update_project_only_description(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        update_project = usecase(code = "PT", new_description = "Descrição do projeto teste")

        assert type(update_project) == Project

        assert repo.projects[1].description == update_project.description