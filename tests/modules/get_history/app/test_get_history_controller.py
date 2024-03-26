from src.modules.get_history.app.get_history_controller import GetHistoryController
from src.modules.get_history.app.get_history_usecase import GetHistoryUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetHistoryController:
    def test_get_history_controller(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'start' : 1100000000000,
            'end' : 1800000000000,
            'amount' : 10,
            'exclusive_start_key' : {'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' : 1634526000000}
            })
        
        response = controller(request)
        assert response.status_code == 200
        assert response.body['message'] == 'the history was retrieved'
        
    def test_get_history_controller_missing_requester_user(self):
            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            'start' : "1612137600000",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'
        
    def test_get_history_controller_wrong_type_user_id(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": 123,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field user_id isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_get_history_controller_invalid_user_id(self):
                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": '12345',
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field user_id is not valid'
                        
    def test_get_history_controller_wrong_type_start(self):
                            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'start' : "1612137600000",
            })
        
        response = controller(request)
        repo_member = MemberRepositoryMock()
        assert response.status_code == 400
        assert response.body == 'Field start isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
                            
    def test_get_history_controller_invalid_start(self):
                                
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'start' : 10,
            })
        
        repo_member = MemberRepositoryMock()
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start is not valid'
                                
    def test_get_history_controller_wrong_type_end(self):
                                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'end' : "1612137600000",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_get_history_controller_invalid_end(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()                               
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'end' : 10,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end is not valid'
        
    def test_get_history_controller_invalid_start_end(self):                                       
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'start' : 1612137600000,
            'end' : 1512137600000,
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start is not valid'
        
    def test_get_history_controller_invalid_exclusive_start_key_action_id(self):                                       
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'exclusive_start_key' : {'action_id' : 'aaaaaaaaa0752-4ce2-9440-05e752e636fc', 'start_date' : "1634526000000"},
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field exclusive_start_key action_id is not valid'
        
    def test_get_history_controller_invalid_exclusive_start_key_start_date(self):                                      
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={ 
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'exclusive_start_key' : {'action_id' : '87d4a661-0752-4ce2-9440-05e752e636fc', 'start_date' :"163452600000000000"}
            })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field exclusive_start_key start_date is not valid'
        
    def test_get_history_controller_wrong_type_amount(self):
        
        repo_member = MemberRepositoryMock()
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'amount' : "20",
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field amount isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_get_history_controller_invalid_amount(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHistoryUsecase(repo, repo_member)
        controller = GetHistoryController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'amount' : 0,
            })
        
        response = controller(request)
        assert response.status_code == 400
        repo_member = MemberRepositoryMock()
        assert response.body == 'Field amount is not valid'