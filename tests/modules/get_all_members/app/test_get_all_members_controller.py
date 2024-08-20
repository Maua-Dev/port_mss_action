from src.modules.get_all_members.app.get_all_members_controller import GetAllMembersController
from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetAllMembersController:

    def test_get_all_members_controller(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        controller = GetAllMembersController(usecase=usecase)
        
        request = HttpRequest(body={
            'requester_user': {
                "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'start_date': 1624576165000,
            'end_date': 1690046000000
        })
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'the members were retrieved'
        assert len(response.body['members']) == 11
    
    def test_get_all_members_controller__requester_user_none(self):
        
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        controller = GetAllMembersController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"