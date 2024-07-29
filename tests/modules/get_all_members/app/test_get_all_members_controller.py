from src.modules.get_all_members.app.get_all_members_controller import GetAllMembersController
from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

class Test_GetAllMembersController:

    def test_get_all_members_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        controller = GetAllMembersController(usecase=usecase)
        request = HttpRequest(body={'requester_user': {
                    "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                    "name": "Vitor Guirão MPNTM",
                    "email": "vsoller@airubio.com",
                    "custom:isMaua": True
                }})
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'the members were retrieved'
        assert len(response.body['members']) == len(repo.get_all_members())
    
    def test_get_all_members_controller__requester_user_none(self):
        
        repo = MemberRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        controller = GetAllMembersController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"