from sqlite3 import Timestamp
from src.modules.update_member.app.update_member_controller import UpdateMemberController
from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateMemberController:
    def test_update_member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },

            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.DISCONNECTED.value,  
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["message"] == "the member was updated"
        assert response.body["member"]["year"] == 3
        
    def test_update_member_controller_only_name(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        user_id = repo.members[0].user_id
        first_member = repo.members[0]
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
            'new_name':"Teste Tester"
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["name"] == "Teste Tester"
        assert response.body["message"] == "the member was updated"

    def test_update_member_controller_only_year(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        request = HttpRequest(body={  
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
       
            'new_year':3
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["year"] == 3
        assert response.body["message"] == "the member was updated"
    
    
    def test_update_member_controller_only_role(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
     
            'new_role':ROLE.HEAD.value
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["role"] == ROLE.HEAD.value
        assert response.body["message"] == "the member was updated"

            

    def test_update_member_controller_invalid_user_id(self):
                    
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        request = HttpRequest(body={
            'requester_user': {
                    "sub": '123234234',
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
            'name':"Joao Branco",
            'email_dev':"jbranco.devmaua@gmail.com",
            'role':ROLE.HEAD.value,
            'stack':STACK.BACKEND.value,
            'year':3,
            'cellphone':"11991152348",
            'course':COURSE.ECM.value,
            'active':ACTIVE.ACTIVE.value
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field user_id is not valid"

    def test_update_member_controller_invalid_year(self):
                    
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        user_id = repo.members[0].user_id
        first_member = repo.members[0]
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':7,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value
            })
        
        response = controller(request)
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_year is not valid"

    def test_update_member_controller_wrong_type_new_name(self):
                        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        user_id = repo.members[0].user_id
        first_member = repo.members[0]
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
            'new_name':123,
            'new_email_dev':"jbranco.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11991152348",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_name isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_member_controller_wrong_type_new_email_dev(self):
                        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        user_id = repo.members[0].user_id
        first_member = repo.members[0]
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },
            'new_name':"Joao Branco",
            'new_email_dev':123,
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11991152348",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field new_email_dev isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
    

    def test_update_member_controller_with_no_request_user(self):
                        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        user_id = repo.members[0].user_id
        first_member = repo.members[0]
        request = HttpRequest(body={
            
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_update_member_controller_another_user(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },

            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value,
            'new_member_user_id': repo.members[2].user_id 
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["message"] == "the member was updated"
        assert response.body["member"]["year"] == 3

    def test_update_member_controller_forbidden_user(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        
        request = HttpRequest(body={
            'requester_user': {
                    "sub": repo.members[5].user_id,
                    "name": repo.members[5].name,
                    "email": repo.members[5].email,
                    "custom:isMaua": True
                },

            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value,
            'new_member_user_id': first_member.user_id 
             
            })
        
        response = controller(request)
       
        assert response.status_code == 403
        assert response.body == 'That type of user has no permission for that action'
        
    def test_update_member_controller_another_user_not_active(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        first_member = repo.members[0]
        first_member.active = ACTIVE.DISCONNECTED
        
        request = HttpRequest(body={
            'requester_user': {
                    "sub": first_member.user_id,
                    "name": first_member.name,
                    "email": first_member.email,
                    "custom:isMaua": True
                },

            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value,
            'new_member_user_id': repo.members[2].user_id 
             
            })
        
        response = controller(request)
       
        assert response.status_code == 403 
        assert response.body == 'That type of user has no permission for that action'
        
    def test_update_member_controller_not_active(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        member = repo.members[2]
        member.active = ACTIVE.DISCONNECTED
        
        request = HttpRequest(body={
            'requester_user': {
                    "sub": member.user_id,
                    "name": member.name,
                    "email": member.email,
                    "custom:isMaua": True
                },

            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value,
            'new_member_user_id': repo.members[2].user_id 
             
            })
        
        response = controller(request)
       
        assert response.status_code == 403
        assert response.body == 'That type of user has no permission for that action'
        
