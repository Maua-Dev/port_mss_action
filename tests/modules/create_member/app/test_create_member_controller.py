from src.modules.create_action.app.create_action_controller import CreateActionController
from src.modules.create_action.app.create_action_usecase import CreateActionUsecase
from src.modules.create_member.app.create_member_controller import CreateMemberController
from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_CreateMemberController:
    def test_create_member_controller(self):
        
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            "name":"Vitor Guirão MPNTM",
            'email_dev':"vsoller.devmaua@gmail.com",
            'email':"vsoller@airubio.com",
            'ra':"21017310",
            'role':'DIRECTOR',
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'hired_date':1614567601000,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the member was created'
        assert response.body['member']['name'] == "Vitor Guirão MPNTM"
        assert response.body['member']['email_dev'] == "vsoller.devmaua@gmail.com"
        assert response.body['member']['email'] == "vsoller@airubio.com"
        assert response.body['member']['ra'] == "21017310"
        assert response.body['member']['role'] == 'DIRECTOR'
        assert response.body['member']['stack'] == STACK.INFRA.value
        assert response.body['member']['year'] == 1
        assert response.body['member']['cellphone'] == "11991758098"
        assert response.body['member']['course'] == COURSE.ECA.value
        assert response.body['member']['hired_date'] == 1614567601000
        assert response.body['member']['active'] == ACTIVE.ACTIVE.value
        assert response.body['member']['deactivated_date'] == None        
    
    def test_create_member_controller_missing_ra(self):
        
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
           'name':"Vitor Guirão MPNTM",
            'email_dev':"vsoller.devmaua@gmail.com",
            'email':"vsoller@airubio.com",
            'role':ROLE.DIRECTOR,
            'stack':STACK.INFRA,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA,
            'hired_date':1614567601000,
            'active':ACTIVE.ACTIVE  ,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field ra is missing'
        
    def test_create_member_controller_missing_name(self):
            
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'email_dev':"vsoller.devmaua@gmail.com",
            'email':"vsoller@airubio.com",
            'ra':"21017310",
            'role':ROLE.DIRECTOR,
            'stack':STACK.INFRA,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA,
            'hired_date':1614567601000,
            'active':ACTIVE.ACTIVE  ,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field name is missing'
        
  
            