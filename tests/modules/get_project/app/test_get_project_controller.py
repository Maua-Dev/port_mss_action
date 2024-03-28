from src.modules.get_project.app.get_project_controller import GetProjectController
from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetProjectController:
    def test_get_project_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={'code': 'MF'})
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'the project was retrieved'
        assert response.body['project']['code'] == 'MF'
        
    def test_get_project_controller_missing_parameters(self):
        
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field code is missing'
        
    def test_get_project_controller_wrong_type_parameters(self):
        
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={'code': 1})
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field code isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_get_project_controller_entity_error(self):
        
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={'code': 'VITOR'})
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field code is not valid'
        
    def test_get_project_controller_no_items_found(self):
        
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={'code': 'AB'})
        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == 'No items found for code'