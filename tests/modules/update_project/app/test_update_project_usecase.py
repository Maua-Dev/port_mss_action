import pytest
from src.modules.update_project.app.update_project_usecase import UpdateProjectUsecase
from src.shared.domain.entities.project import Project
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction, UnregisteredUser, UserNotAllowed
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.enums.active_enum import ACTIVE

class TestUpdateProjectUsecase:

    def test_update_project(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        update_project = usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_scrum_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_photos = ["foto1", "foto2"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"], user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae3")

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_user_id == update_project.po_user_id
        assert repo.projects[1].scrum_user_id == update_project.scrum_user_id
        assert repo.projects[1].photos == update_project.photos


    def test_update_project_one_parameter(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        update_project = usecase(code = "PT", new_name = "Novo nome", new_description = "É um site", new_po_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_scrum_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_photos = ["https://i.imgur.com/gHoRKJU.png"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"], user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae3")

        assert type(update_project) == Project

        assert repo.projects[1].name == update_project.name
        assert repo.projects[1].description == update_project.description
        assert repo.projects[1].po_user_id == update_project.po_user_id
        assert repo.projects[1].scrum_user_id == update_project.scrum_user_id
        assert repo.projects[1].photos == update_project.photos

    def test_update_project_not_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)

        with pytest.raises(NoItemsFound):
            usecase(code = "RR", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "6574hgyt-785n-9134-18gn4-7gh5uvn36cG", new_scrum_user_id = "7gh5yf5H-857H-1234-75hng-94832hvng1s", new_photos = ["foto1", "foto2"], user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae3")

    def test_update_project_only_description(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        update_project = usecase(code = "PT", new_description = "Descrição do projeto teste", user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae3")

        assert type(update_project) == Project

        assert repo.projects[1].description == update_project.description

    def test_update_project_no_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)

        with pytest.raises(UnregisteredUser):
            usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_scrum_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_photos = ["foto1", "foto2"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"], user_id = "93bc6ada-c0d1-7054-66ab-e17414c48ae4")

    def test_update_project_forbidden_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)

        with pytest.raises(UserNotAllowed):
            usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_scrum_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_photos = ["foto1", "foto2"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"], user_id = repo_member.members[2].user_id)
              
    def test_update_project_FREEZE_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        user = repo_member.members[0]
        user.active= ACTIVE.FREEZE
        with pytest.raises(UserNotAllowed):
            usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_scrum_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_photos = ["foto1", "foto2"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"], user_id = user.user_id)
    
    def test_update_project_DISCONNECTED_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        user = repo_member.members[0]
        user.active= ACTIVE.DISCONNECTED
        with pytest.raises(UserNotAllowed):
            usecase(code = "PT", new_name = "Projeto Teste", new_description = "Descrição do projeto teste", new_po_user_id = "51ah5jaj-c9jm-1345-666ab-e12341c14a3", new_scrum_user_id = "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", new_photos = ["foto1", "foto2"], new_members_user_ids = ["51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"], user_id = user.user_id)
                         