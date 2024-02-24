from src.modules.batch_get_member.app.batch_get_member_controller import BatchGetMemberController
from src.modules.batch_get_member.app.batch_get_member_usecase import BatchGetMemberUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_BatchGetMemberController:
    def test_batch_get_member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        first_member = repo.members[0]
        second_member = repo.members[1]
        third_member = repo.members[2]
        request = HttpRequest(body={
            'requester_user': {
                "sub": first_member.user_id,
                "name": first_member.name,
                "email": first_member.email,
                "custom:isMaua": True
            },
            'user_ids': [second_member.user_id, third_member.user_id]
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['members'][0]['user_id'] == repo.members[1].user_id
        assert response.body['members'][1]['user_id'] == repo.members[2].user_id
        
        
    def test_batch_get_member_controller_user_ids_is_none(self): 
        
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        first_member = repo.members[0]
        second_member = repo.members[1]
        third_member = repo.members[2]
        request = HttpRequest(body={
            'requester_user': {
                "sub": first_member.user_id,
                "name": first_member.name,
                "email": first_member.email,
                "custom:isMaua": True
            },
            'user_ids': [None]
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field user_id is missing"
        
    def test_batch_get_member_controller_wrong_type_user_id(self):
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        first_member = repo.members[0]
        second_member = repo.members[1]
        third_member = repo.members[2]
        request = HttpRequest(body={
            'requester_user': {
                "sub": first_member.user_id,
                "name": first_member.name,
                "email": first_member.email,
                "custom:isMaua": True
            },
            'user_ids': [[]]
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field user_id isn't in the right type.\n Received: <class 'list'>.\n Expected: str"
            
    def test_batch_get_member_controller_invalid_user_id(self):
       
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        first_member = repo.members[0]
        second_member = repo.members[1]
        third_member = repo.members[2]
        request = HttpRequest(body={
            'requester_user': {
                "sub": first_member.user_id,
                "name": first_member.name,
                "email": first_member.email,
                "custom:isMaua": True
            },
            'user_ids': ['1234batata', 1234]
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field user_id is not valid"
        
    def test_batch_get_member_controller_no_items_found(self): 
        
        repo = MemberRepositoryMock()
        usecase = BatchGetMemberUsecase(repo=repo)
        controller = BatchGetMemberController(usecase=usecase)
        first_member = repo.members[0]
        second_member = repo.members[1]
        third_member = repo.members[2]
        request = HttpRequest(body={
            'requester_user': {
                "sub": first_member.user_id,
                "name": first_member.name,
                "email": first_member.email,
                "custom:isMaua": True
            },
            'user_ids': ['13bc6bda-c0d1-7054-66ab-e17414c48ae3','23bc6ada-c0d1-7054-66ab-e17414c48ae3']
        })

        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == "No items found for user_ids"