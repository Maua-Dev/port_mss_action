from src.modules.get_history.app.get_history_controller import GetHistoryController
from src.modules.get_history.app.get_history_usecase import GetHistoryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetHistoryController:
    def test_get_history_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra': '21010757',
            })
        
        response = controller(request)
        assert response.status_code == 200
        assert response.body['message'] == 'the history was retrieved'
        
    def test_get_history_controller_missing_ra(self):
            
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'start' : 1612137600000,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field ra is missing'
        
    def test_get_history_controller_wrong_type_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : 21010757,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field ra isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_get_history_controller_invalid_ra(self):
                        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '12345',
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field ra is not valid'
                        
    def test_get_history_controller_wrong_type_start(self):
                            
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'start' : '1612137600000',
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
                            
    def test_get_history_controller_invalid_start(self):
                                
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'start' : 10,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start is not valid'
                                
    def test_get_history_controller_wrong_type_end(self):
                                        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'end' : '1612137600000',
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_get_history_controller_invalid_end(self):                                       
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'end' : 10,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end is not valid'
        
    def test_get_history_controller_invalid_start_end(self):                                       
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'start' : 1612137600000,
            'end' : 1512137600000,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start is not valid'
        
    def test_get_history_controller_invalid_exclusive_start_key(self):                                       
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'exclusive_start_key' : '1512137600000',
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field exclusive_start_key is not valid'
        
    def test_get_history_controller_wrong_type_amount(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'amount' : '20',
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field amount isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_get_history_controller_invalid_amount(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra' : '21010757',
            'amount' : 0,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field amount is not valid'

    def test_get_history_controller_no_items_found(self):
            
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'ra': '21010757',
            'start': 1612137600000,
            'end': 1612137600000,
            'amount': 1
            })
        
        response = controller(request)
        assert response.status_code == 404
        assert response.body == 'No items found for ra'