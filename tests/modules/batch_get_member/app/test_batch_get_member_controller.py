from src.modules.batch_get_member.app.batch_get_member_controller import BatchGetMemberController
from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_BatchGetMemberController:
    def test_batch_get_member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'user_ids': [repo.members[0].user_id, repo.members[1].user_id]})
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['members'][0]['user_id'] == repo.members[0].user_id
        assert response.body['members'][1]['user_id'] == repo.members[1].user_id
        
    def test_batch_get_member_controller_ras_is_none(self): 
        
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={})
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field user_ids is missing"
        
    def test_batch_get_member_controller_wrong_type_ra(self):
            
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'user_ids': [22011020]})

        response = controller(request=request)

        # assert response.status_code == 400
        assert response.body == "Field user_id isn\'t in the right type.\n Received: <class 'int'>.\n Expected: str"
            
    def test_batch_get_member_controller_invalid_ra(self):
            
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'user_ids': ['123']})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field user_id is not valid"
        
    def test_batch_get_member_controller_no_items_found(self): 
        
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        request = HttpRequest(body={'user_ids': ['9183jBnh-997H-1020-10god-914gHy46tBh']})
        
        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == "No items found for user_ids"