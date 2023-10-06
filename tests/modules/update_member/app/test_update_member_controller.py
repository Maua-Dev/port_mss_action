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
    def test_update_Member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        first_user = repo.members[0]
        request = HttpRequest(body={
            'ra': ra,
            'new_name':"Teste Tester",
            'new_email_dev':"test.devmaua@gmail.com",
            'new_role':ROLE.HEAD.value,
            'new_stack':STACK.BACKEND.value,
            'new_year':3,
            'new_cellphone':"11987654321",
            'new_course':COURSE.ECM.value,
            'new_active':ACTIVE.ACTIVE.value,
            'new_deactivated_date': 16345761650222  
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["deactivated_date"] == 16345761650222
        assert response.body["message"] == "the member was updated"

    def test_update_Member_controller_only_name(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        first_user = repo.members[0]
        request = HttpRequest(body={
            'ra': ra,
            'new_name':"Teste Tester"
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["name"] == "Teste Tester"
        assert response.body["message"] == "the member was updated"

    def test_update_Member_controller_only_year(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        first_user = repo.members[0]
        request = HttpRequest(body={
            'ra': ra,
            'new_year':3
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["year"] == 3
        assert response.body["message"] == "the member was updated"
    
    
    def test_update_Member_controller_only_role(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        first_user = repo.members[0]
        request = HttpRequest(body={
            'ra': ra,
            'new_role':ROLE.HEAD.value
             
            })
        
        response = controller(request)
       
        assert response.status_code == 200
        assert response.body["member"]["role"] == ROLE.HEAD.value
        assert response.body["message"] == "the member was updated"

    def test_update_member_controller_missing_ra(self):
            
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)

        request = HttpRequest(body={
            'new_name':"Joao Branco",
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
        assert response.body == "Field ra is missing"
            
    def test_update_member_controller_wrong_type_ra(self):
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)

        request = HttpRequest(body={
            'ra': 123234234,
            'new_name':"Joao Branco",
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
        assert response.body == 'Field ra isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_member_controller_invalid_ra(self):
                    
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        request = HttpRequest(body={
            'ra': '123234234',
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
        assert response.body == "Field ra is not valid"
        
    def test_update_member_controller_wrong_type_new_name(self):
                        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        request = HttpRequest(body={
            'ra': ra,
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
        ra = repo.members[0].ra
        request = HttpRequest(body={
            'ra': ra,
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
        
    def test_update_member_controller_deactivate_date_sooner_than_hired_date(self):
                        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        request = HttpRequest(body={
            'ra': ra,
            'new_deactivated_date':1
            })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field new_deactivated_date is not valid"