from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetAllProjectsUsecase:
    def test_get_all_projects_usecase(self):
        repo = ActionRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo)
        
        projects = usecase()
        assert type(projects) == list
        assert len(projects) == 5
        assert type(projects[0]) == Project