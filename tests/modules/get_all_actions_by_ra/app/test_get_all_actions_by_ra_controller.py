from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_controller import GetAllActionsByRaController
from src.modules.get_all_actions_by_ra.app.get_all_actions_by_ra_usecase import GetAllActionsByRaUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_GetAllActionsByRaController:
    def test_get_all_actions_by_ra_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo=repo)
        controller = GetAllActionsByRaController(usecase=usecase)
        request = HttpRequest(query_params={'ra': '21017310'})
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'actions retrieved with success'
        assert len(response.body['actions']) == 4
    
    def test_get_all_actions_by_ra_controller_missing_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = GetAllActionsByRaUsecase(repo=repo)
        controller = GetAllActionsByRaController(usecase=usecase)
        request = HttpRequest(query_params={})
        
        response = controller(request=request)
        
        assert response.status_code == 400
        