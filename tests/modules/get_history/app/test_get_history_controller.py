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
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'start' : 1100000000000,
            'end' : 1800000000000,
            'amount' : 10,
            'exclusive_start_key' : {'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' : 1634526000000}
            })
        
        response = controller(request)
        assert response.status_code == 200
        assert response.body['message'] == 'the history was retrieved'
        
    def test_get_history_controller_missing_user_id(self):
            
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'start' : "1612137600000",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field user_id is missing'
        
    def test_get_history_controller_wrong_type_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id' : 21010757,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field user_id isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_get_history_controller_invalid_user_id(self):
                        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id' : '12345',
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field user_id is not valid'
                        
    def test_get_history_controller_wrong_type_start(self):
                            
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'start' : "1612137600000",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
                            
    def test_get_history_controller_invalid_start(self):
                                
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
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
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'end' : "1612137600000",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_get_history_controller_invalid_end(self):                                       
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
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
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'start' : 1612137600000,
            'end' : 1512137600000,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start is not valid'
        
    def test_get_history_controller_invalid_exclusive_start_key_action_id(self):                                       
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'exclusive_start_key' : {'action_id' : 'aaaaaaaaa0752-4ce2-9440-05e752e636fc', 'start_date' : "1634526000000"},
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field exclusive_start_key action_id is not valid'
        
    def test_get_history_controller_invalid_exclusive_start_key_start_date(self):                                      
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={ 
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'exclusive_start_key' : {'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' :"163452600000000000"}
            })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field exclusive_start_key start_date is not valid'
        
    def test_get_history_controller_wrong_type_amount(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'amount' : "20",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field amount isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_get_history_controller_invalid_amount(self):
        
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'amount' : 0,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field amount is not valid'