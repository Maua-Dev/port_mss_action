from src.modules.portfolio_export_projects.app.portfolio_export_projects_usecase import PortfolioExportProjectsUsecase
from src.modules.portfolio_export_projects.app.portfolio_export_projects_viewmodel import PortfolioExportProjectsViewModel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.domain.entities.project import Project


class Test_PortfolioExportProjectsViewModel:
    def test_portfolio_export_projects_viewmodel(self):
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportProjectsUsecase(action_repo)

        projects = usecase()
        viewmodel = PortfolioExportProjectsViewModel(projects=projects).to_dict()

        assert 'projects' in viewmodel
        assert len(viewmodel['projects']) == len(projects)

        first_project = viewmodel['projects'][0]
        assert set(first_project.keys()) == {'code', 'name', 'description', 'photo'}
        assert first_project['code'] == projects[0].code
        assert first_project['name'] == projects[0].name
        assert first_project['description'] == projects[0].description
        assert first_project['photo'] == (projects[0].photo if projects[0].photo is not None else "")

    def test_portfolio_export_projects_viewmodel_empty_list(self):
        viewmodel = PortfolioExportProjectsViewModel(projects=[]).to_dict()

        assert 'projects' in viewmodel
        assert len(viewmodel['projects']) == 0
        assert len(viewmodel.keys()) == 1

    def test_portfolio_export_projects_viewmodel_photo_none_becomes_empty_string(self):
        project = Project(
            code="SF",
            name="Selfie Mauá",
            description="Aplicativo para reconhecimento facial",
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
            start_date=1686754800000,
            members_user_ids=["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            photo=None
        )

        viewmodel = PortfolioExportProjectsViewModel(projects=[project]).to_dict()

        assert viewmodel['projects'][0]['photo'] == ""
        assert 'po_user_id' not in viewmodel['projects'][0]
        assert 'scrum_user_id' not in viewmodel['projects'][0]
        assert 'start_date' not in viewmodel['projects'][0]
        assert 'members_user_ids' not in viewmodel['projects'][0]

    def test_portfolio_export_projects_viewmodel_keeps_photo_url(self):
        project = Project(
            code="MF",
            name="Maua Food",
            description="É um aplicativo #foramoleza",
            po_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            scrum_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            start_date=1634576165000,
            members_user_ids=["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"],
            photo="https://i.imgur.com/gHoRKJU.png"
        )

        viewmodel = PortfolioExportProjectsViewModel(projects=[project]).to_dict()

        assert viewmodel['projects'][0]['photo'] == "https://i.imgur.com/gHoRKJU.png"

    def test_portfolio_export_projects_viewmodel_maps_all_projects(self):
        action_repo = ActionRepositoryMock()
        projects = action_repo.projects
        viewmodel = PortfolioExportProjectsViewModel(projects=projects).to_dict()

        assert len(viewmodel['projects']) == len(projects)
        for index, project in enumerate(projects):
            exported = viewmodel['projects'][index]
            assert exported['code'] == project.code
            assert exported['name'] == project.name
            assert exported['description'] == project.description
            assert exported['photo'] == (project.photo if project.photo is not None else "")
            assert set(exported.keys()) == {'code', 'name', 'description', 'photo'}
