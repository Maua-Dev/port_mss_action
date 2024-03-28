from src.modules.get_all_projects.app.get_all_projects_controller import GetAllProjectsController
from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetAllProjectsController:
    def test_get_all_projects_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = GetAllProjectsUsecase(repo=repo)
        controller = GetAllProjectsController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'the projects were retrieved'
        assert len(response.body['projects']) == len(repo.projects)