import pytest
from src.modules.update_project.app.update_project_controller import UpdateProjectController
from src.modules.update_project.app.update_project_usecase import UpdateProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

class TestUpdateProjectController:

    def test_update_project_controller(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                'new_scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                'new_photo': 'new_photo',
                'new_members_user_ids': ['6574hgyt-785n-9134-18gn4-7gh5uvn36cG', '7gh5yf5H-857H-1234-75hng-94832hvng1s']
            }
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body['project']['code'] == 'PT'
        assert response.body['project']['name'] == 'Portfolio'
        assert response.body['project']['description'] == 'Projeto do site portfolio'
        assert response.body['project']['po_user_id'] == '6574hgyt-785n-9134-18gn4-7gh5uvn36cG'
        assert response.body['project']['scrum_user_id'] == '7gh5yf5H-857H-1234-75hng-94832hvng1s'
        assert response.body['project']['photo'] == ['new_photo']
        assert response.body['project']['members_user_ids'] == ['6574hgyt-785n-9134-18gn4-7gh5uvn36cG', '7gh5yf5H-857H-1234-75hng-94832hvng1s']

    def test_update_project_controller_missing_code(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                'new_scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                'new_photo': 'new_photo',
                'new_members_user_ids': ['6574hgyt-785n-9134-18gn4-7gh5uvn36cG', '7gh5yf5H-857H-1234-75hng-94832hvng1s']
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'

    def test_update_project_controller_project_not_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'RR',
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                'new_scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                'new_photo': 'new_photo',
                'new_members_user_ids': ['6574hgyt-785n-9134-18gn4-7gh5uvn36cG', '7gh5yf5H-857H-1234-75hng-94832hvng1s']
            }
        )

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for project'

    def test_update_project_controller_code_not_valid(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 25,
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                'new_scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                'new_photo': 'new_photo',
                'new_members_user_ids': ['6574hgyt-785n-9134-18gn4-7gh5uvn36cG', '7gh5yf5H-857H-1234-75hng-94832hvng1s']
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'

    def test_update_project_controller_only_description(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_description': 'Projeto do site portfolio'
            }
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body['project']['code'] == 'PT'
        assert response.body['project']['description'] == 'Projeto do site portfolio'

    def test_update_project_controller_invalid_name(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_name': 25
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name is not valid"
    
    def test_update_project_controller_invalid_description(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_description': 25
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field description is not valid"
        
    def test_update_project_controller_invalid_po_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_po_user_id': 25
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field po_user_id is not valid"
        
    def test_update_project_controller_invalid_scrum_user_id(self): 
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_scrum_user_id': 25
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field scrum_user_id is not valid"
        
    def test_update_project_controller_invalid_photo(self): 
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": repo_member.members[0].user_id,
                    "name": repo_member.members[0].name,
                    "email": repo_member.members[0].email,
                    "custom:isMaua": True
            },
                'code': 'PT',
                'new_photo': 25
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field photo is not valid"

    def test_update_project_missing_requester_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateProjectUsecase(repo, repo_member)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                'code': 'PT',
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                'new_scrum_user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                'new_photo': 'new_photo',
                'new_members_user_ids': ['6574hgyt-785n-9134-18gn4-7gh5uvn36cG', '7gh5yf5H-857H-1234-75hng-94832hvng1s']
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'