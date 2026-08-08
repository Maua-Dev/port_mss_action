from src.modules.portfolio_export_projects.app.portfolio_export_projects_usecase import PortfolioExportProjectsUsecase
from src.shared.domain.entities.project import Project
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_PortfolioExportProjectsUsecase:
    def test_portfolio_export_projects_usecase(self):
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportProjectsUsecase(action_repo=action_repo)

        projects = usecase()

        assert type(projects) == list
        assert len(projects) > 0
        assert type(projects[0]) == Project
        assert len(projects) == len(action_repo.projects)

    def test_portfolio_export_projects_usecase_returns_all_projects(self):
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportProjectsUsecase(action_repo=action_repo)

        projects = usecase()

        expected_codes = [project.code for project in action_repo.projects]
        actual_codes = [project.code for project in projects]

        assert actual_codes == expected_codes

    def test_portfolio_export_projects_usecase_empty_list(self):
        action_repo = ActionRepositoryMock()
        action_repo.projects = []
        usecase = PortfolioExportProjectsUsecase(action_repo=action_repo)

        projects = usecase()

        assert projects == []

    def test_portfolio_export_projects_usecase_preserves_project_data(self):
        action_repo = ActionRepositoryMock()
        usecase = PortfolioExportProjectsUsecase(action_repo=action_repo)

        projects = usecase()
        first_project = projects[0]
        expected = action_repo.projects[0]

        assert first_project.code == expected.code
        assert first_project.name == expected.name
        assert first_project.description == expected.description
        assert first_project.photo == expected.photo
