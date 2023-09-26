from src.modules.batch_get_member.app.batch_get_member_controller import BatchGetMemberController
from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_BatchGetMemberController:
    def test_batch_get_member_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'ras': [repo.members[0].ra, repo.members[1].ra]})
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['members'][0]['ra'] == repo.members[0].ra
        assert response.body['members'][1]['ra'] == repo.members[1].ra
        
    def test_batch_get_member_controller_ras_is_none(self): 
        
        repo = ActionRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={})
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field ras is missing"
        
    def test_batch_get_member_controller_wrong_type_ra(self):
            
        repo = ActionRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'ras': [22011020]})

        response = controller(request=request)

        # assert response.status_code == 400
        assert response.body == "Field ra isn\'t in the right type.\n Received: <class 'int'>.\n Expected: str"
            
    def test_batch_get_member_controller_invalid_ra(self):
            
        repo = ActionRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'ras': ['123']})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"
        
    def test_batch_get_member_controller_no_items_found(self): 
        
        repo = ActionRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'ras': ['22011020']})
        
        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == "No items found for ras"