from src.modules.portfolio_export_projects.app.portfolio_export_projects_controller import PortfolioExportProjectsController
from src.modules.portfolio_export_projects.app.portfolio_export_projects_usecase import PortfolioExportProjectsUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest


class Test_PortfolioExportProjectsController:
    action_repo = ActionRepositoryMock()
    usecase = PortfolioExportProjectsUsecase(action_repo=action_repo)
    controller = PortfolioExportProjectsController(usecase)

    def test_portfolio_export_projects_controller(self):
        request = HttpRequest(body={})

        response = self.controller(request)

        assert response.status_code == 200
        assert 'projects' in response.body
        assert len(response.body['projects']) > 0

        first_project = response.body['projects'][0]
        assert set(first_project.keys()) == {'code', 'name', 'description', 'photo'}

    def test_portfolio_export_projects_controller_with_no_body(self):
        request = HttpRequest()

        response = self.controller(request)

        assert response.status_code == 200
        assert 'projects' in response.body

    def test_portfolio_export_projects_controller_returns_all_projects(self):
        request = HttpRequest(body={})

        response = self.controller(request)

        assert response.status_code == 200
        assert len(response.body['projects']) == len(self.action_repo.projects)
        assert response.body['projects'][0]['code'] == self.action_repo.projects[0].code
        assert response.body['projects'][0]['name'] == self.action_repo.projects[0].name

    def test_portfolio_export_projects_controller_does_not_require_requester_user(self):
        request = HttpRequest(body={"some_unrelated_field": "value"})

        response = self.controller(request)

        assert response.status_code == 200
        assert 'projects' in response.body

    def test_portfolio_export_projects_controller_response_values(self):
        request = HttpRequest(body={})

        response = self.controller(request)
        expected = self.action_repo.projects[0]

        assert response.status_code == 200
        assert response.body['projects'][0]['code'] == expected.code
        assert response.body['projects'][0]['name'] == expected.name
        assert response.body['projects'][0]['description'] == expected.description
        assert response.body['projects'][0]['photo'] == (expected.photo if expected.photo is not None else "")
