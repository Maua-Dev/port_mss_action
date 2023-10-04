
import uuid
from src.modules.update_action.app.update_action_controller import UpdateActionController
from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.modules.update_member.app.update_member_controller import UpdateMemberController
from src.modules.update_member.app.update_member_usecase import UpdateMemberUsecase
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateMemberController:
    def test_update_Member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        request = HttpRequest(body={
            'ra': ra,
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
        assert response.status_code == 200
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
        assert response.body == "Field ra is not valid"
        
    def test_update_member_controller_wrong_type_new_name(self):
                        
        repo = MemberRepositoryMock()
        usecase = UpdateMemberUsecase(repo)
        controller = UpdateMemberController(usecase)
        ra = repo.members[0].ra
        request = HttpRequest(body={
             'ra': ra,
            'new_name':234,
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
        assert response.body == 'Field new_name isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
 