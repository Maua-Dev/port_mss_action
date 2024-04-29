from src.modules.get_project.app.get_project_controller import GetProjectController
from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetProjectController:
    def test_get_project_controller(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={
            'requester_user': {
                'sub': repo_member.members[0].user_id,
                'name': repo_member.members[0].name,
                'email': repo_member.members[0].email,
                'custom:isMaua': True
            },
            'code': 'MF'
        })
        response = controller(request=request)
        
        assert response.status_code == 200
        assert response.body['message'] == 'the project was retrieved'
        assert response.body['project']['code'] == 'MF'
        
    def test_get_project_controller_missing_parameters(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={
            'requester_user': {
                'sub': repo_member.members[0].user_id,
                'name': repo_member.members[0].name,
                'email': repo_member.members[0].email,
                'custom:isMaua': True
            },
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field code is missing'
        
    def test_get_project_controller_wrong_type_parameters(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={
            'requester_user': {
                'sub': repo_member.members[0].user_id,
                'name': repo_member.members[0].name,
                'email': repo_member.members[0].email,
                'custom:isMaua': True
            },
            'code': 1
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field code isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_get_project_controller_entity_error(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={
            'requester_user': {
                'sub': repo_member.members[0].user_id,
                'name': repo_member.members[0].name,
                'email': repo_member.members[0].email,
                'custom:isMaua': True
            },
            'code': 'VITOR'
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field code is not valid'
        
    def test_get_project_controller_no_items_found(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={
            'requester_user': {
                'sub': repo_member.members[0].user_id,
                'name': repo_member.members[0].name,
                'email': repo_member.members[0].email,
                'custom:isMaua': True
            },
            'code': 'AB'
        })
        response = controller(request=request)
        
        assert response.status_code == 404
        assert response.body == 'No items found for code'

    def test_get_project_controller_no_user_found(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetProjectUsecase(repo=repo, repo_member=repo_member)
        controller = GetProjectController(usecase=usecase)
        request = HttpRequest(body={
            'code': 'MF'
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'