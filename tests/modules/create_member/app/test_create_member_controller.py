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
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão Mpntm",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the member was created'
        assert response.body['member']['name'] == "Vitor Guirão Mpntm"
        assert response.body['member']['email_dev'] == "vsoller.devmaua@gmail.com"
        assert response.body['member']['email'] == "vsoller@airubio.com"
        assert response.body['member']['ra'] == "21017315"
        assert response.body['member']['role'] == 'DIRECTOR'
        assert response.body['member']['stack'] == STACK.INFRA.value
        assert response.body['member']['year'] == 1
        assert response.body['member']['cellphone'] == "11991758098"
        assert response.body['member']['course'] == COURSE.ECA.value
        assert response.body['member']['active'] == ACTIVE.ONHOLD.value
        assert response.body['member']['user_id'] == "13bc6ada-c0d1-7054-66ab-e17414c48ae3"     
    
    def test_create_member_controller_missing_ra(self):
        
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field ra is missing'
        

        
    def test_create_member_controller_invalid_email_dev(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.d.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field email_dev is not valid"  
            
    def test_create_member_controller_invalid_email(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "email": "",
                "name": "Vitor Guirão MPNTM",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
 
       
    def test_create_member_controller_invalid_ra(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017ertert315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field ra is not valid"  

    def test_create_member_controller_invalid_role(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':'ROLE',
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field role is not valid"  

    def test_create_member_controller_invalid_stack(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':'STACK.INFRA.value',
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field stack is not valid"  

    def test_create_member_controller_invalid_year(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':56,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field year is not valid"  

    def test_create_member_controller_invalid_cellphone(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"18098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field cellphone is not valid"  

    def test_create_member_controller_invalid_course(self):
                    
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
               "requester_user": {
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':'COURSE.ECA.value',
            'deactivated_date':None
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field course is not valid"    
 
    def test_create_member_controller_missing_requester_user(self):
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
              
            'email_dev':"vsoller.devmaua@gmail.com",
            'ra':"21017315",
            'role':ROLE.DIRECTOR.value,
            'stack':STACK.INFRA.value,
            'year':1,
            'cellphone':"11991758098",
            'course':COURSE.ECA.value,
            'deactivated_date':None
        })
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"  