import uuid
from src.modules.update_action.app.update_action_controller import UpdateActionController
from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateActionController:
    def test_update_action_controller(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,    
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_duration' : 1000000,
            'new_is_valid': True
            })
        
        response = controller(request)
        assert response.status_code == 200
        assert response.body["message"] == "the action was updated"
        
    def test_update_action_controller_missing_action_id(self):
            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field action_id is missing"
            
    def test_update_action_controller_wrong_type_action_id(self):
                
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': 1,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_id isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_controller_invalid_id(self):
                    
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': 'não-sou-um-uuid',
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field action_id is not valid"
        
    def test_update_action_controller_wrong_type_new_user_id(self):
                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": 123,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field user_id isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_controller_invalid_new_user_id(self):
                            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": "não-sou-um-uuid",
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field user_id is not valid"
        
    def test_update_action_controller_wrong_type_new_start_date(self):
                                
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : '1634526000000',
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_start_date isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_update_action_controller_invalid_new_start_date(self):
                                    
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 100,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_start_date is not valid"
        
    def test_update_action_controller_wrong_type_new_end_date(self):
                                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : '1634536800000',
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_end_date isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_update_action_controller_invalid_new_end_date(self):
                                            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 100,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_end_date is not valid"
        
    def test_update_action_controller_invalid_new_start_and_end_date(self):
                                                
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634536800000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634526000000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_start_date and new_end_date is not valid"
        
    def test_update_action_controller_wrong_type_new_duration(self):
                                                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_duration' : '100',
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_duration isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_update_action_controller_invalid_new_duration(self):
                                                            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_duration' : -100,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_duration is not valid"
        
    def test_update_action_controller_invalid_duration_2(self): # duration greater than end_date - start_date
                                                                
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_duration' : 20800000
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_duration is not valid"
        
    def test_update_action_controller_wrong_type_new_story_id(self):
                                                                    
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : '100',
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_story_id isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: int'
        
    def test_update_action_controller_invalid_new_story_id(self):
                                                                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : -100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_story_id is not valid"
        
    def test_update_action_controller_wrong_type_new_title(self):
                                                                            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : 100,
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_title isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_controller_invalid_new_title(self):
                                                                                
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        long_title = "a" * 101
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : long_title,
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_title is not valid"
        
    def test_update_action_controller_wrong_type_new_description(self):
                                                                                    
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : 100,
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_description isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_controller_invalid_new_description(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        long_description = "a" * 501
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : long_description,
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_description is not valid"
        
    def test_update_action_controller_wrong_type_new_project_code(self):
                                                                                        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : 100,
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_project_code isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_controller_invalid_new_project_code(self):
                                                                                            
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "ABC",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_project_code is not valid"
        
    def test_update_action_controller_wrong_type_new_associated_members_user_ids(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_associated_members_user_ids isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: list'
        
    def test_update_action_controller_wrong_type_new_associated_members_user_ids(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        
        
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : [123],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_associated_members_user_ids isn't in the right type.\n Received: <class 'int'>.\n Expected: str"
        
    def test_update_action_controller_invalid_new_associated_members_user_ids(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        
        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["2201102"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_associated_members_user_ids is not valid"
        
    def test_update_action_controller_wrong_type_new_stack_tags(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id


        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : "BACKEND",
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_stack_tags isn\'t in the right type.\n Received: <class \'str\'>.\n Expected: list'
        
    def test_update_action_controller_wrong_type_stack_tag_new_stack_tags(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id


        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : [1],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_stack_tags isn't in the right type.\n Received: <class 'int'>.\n Expected: str"
        
    def test_update_action_controller_invalid_new_stack_tags(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id


        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACK"],
            'new_action_type_tag' : "CODE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_stack_tags is not valid"
        
    def test_update_action_controller_wrong_type_new_action_type_tag(self):    
           
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id


        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : 1
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_action_type_tag isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_controller_invalid_new_action_type_tag(self):   
           
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id


        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "TESTE"
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_action_type_tag is not valid"
        
    def test_update_action_controller_action_not_found(self):   
           
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = str(uuid.uuid4())

        request = HttpRequest(body={
            'action_id': action_id,
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_is_valid': True
        })

        response = controller(request)
        assert response.status_code == 404
        assert response.body == "No items found for action"
        
    def test_update_action_controller_with_none_story_id(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : None,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : "Teste",
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_is_valid': True
        })
        response = controller(request)
        print(response.body)
        assert response.status_code == 200
        assert response.body["message"] == "the action was updated"
        assert response.body['action']['story_id'] == None
        
    def test_update_action_controller_with_none_description(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_description' : None,
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_is_valid': True
        })
        response = controller(request)
        assert response.status_code == 200
        assert response.body["message"] == "the action was updated"
        assert response.body['action']['description'] == None

    def test_update_action_controller_another_user(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[0].user_id,
                "name": repo_member.members[0].name,
                "email": repo_member.members[0].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_duration' : 1000000,
            'new_is_valid': True,
            "new_member_user_id": repo_member.members[1].user_id
            })
        
        response = controller(request)
        assert response.status_code == 200
        assert response.body["message"] == "the action was updated"

    def test_update_action_controller_another_user(self):
        
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member)
        controller = UpdateActionController(usecase)
        action_id = repo.actions[0].action_id
        user_id = repo.actions[0].action_id

        request = HttpRequest(body={
            "requester_user": {
                "sub": repo_member.members[2].user_id,
                "name": repo_member.members[2].name,
                "email": repo_member.members[2].email,
                "custom:isMaua": True
            },
            'action_id': action_id,
            'new_start_date' : 1634526000000,
            'new_story_id' : 100,
            'new_associated_members_user_ids' : ["6574hgyt-785n-9134-18gn4-7gh5uvn36cG"],
            'new_title' : "Teste",
            'new_end_date' : 1634536800000,
            'new_project_code' : "MF",
            'new_stack_tags' : ["BACKEND"],
            'new_action_type_tag' : "CODE",
            'new_duration' : 1000000,
            'new_is_valid': True,
            "new_member_user_id": repo_member.members[0].user_id
            })
        
        response = controller(request)
        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this This user can´t update this action. He is not the owner of the action or an admin.'