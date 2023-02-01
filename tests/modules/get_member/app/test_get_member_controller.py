from src.modules.get_member.app.get_member_controller import GetMemberController
from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_GetMemberController:
    def test_get_member_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        controller = GetMemberController(usecase=usecase)
        request = HttpRequest(query_params={'ra': repo.members[0].ra})
        
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['member']['ra'] == repo.members[0].ra
        assert response.body['member']['name'] == repo.members[0].name
        assert response.body['member']['email'] == repo.members[0].email
        assert response.body['member']['cellphone'] == repo.members[0].cellphone
        assert response.body['member']['role'] == repo.members[0].role.value
        assert response.body['member']['stack'] == repo.members[0].stack.value
        assert response.body['member']['year'] == repo.members[0].year
        assert response.body['member']['course'] == repo.members[0].course.value
        assert response.body['member']['hired_date'] == repo.members[0].hired_date
        assert response.body['member']['deactivated_date'] == repo.members[0].deactivated_date
        assert response.body['member']['active'] == repo.members[0].active.value
        assert response.body['member']['projects'][0]['code'] == repo.members[0].projects[0].code
        assert response.body['member']['projects'][0]['name'] == repo.members[0].projects[0].name
        assert response.body['member']['projects'][0]['description'] == repo.members[0].projects[0].description
        assert response.body['message'] == "the member was retrieved"
    
    def test_get_member_controller_ra_is_none(self):
        
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        controller = GetMemberController(usecase=usecase)
        request = HttpRequest(query_params={})
        
        response = controller(request=request)       
        
        assert response.status_code == 400
        assert response.body == "Field ra is missing"
    
    def test_get_member_controller_invalid_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        controller = GetMemberController(usecase=usecase)
        request = HttpRequest(query_params={'ra': '123'})
        
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field ra is not valid"
    
    def test_get_member_controller_no_items_found(self):
        
        repo = ActionRepositoryMock()
        usecase = GetMemberUsecase(repo=repo)
        controller = GetMemberController(usecase=usecase)
        request = HttpRequest(query_params={'ra': '12345678'})
        
        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == "No items found for member"