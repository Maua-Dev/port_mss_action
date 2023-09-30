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
            'name':"Vitor Guirão MPNTM",
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
        assert response.status_code == 201
        assert response.body['message'] == 'the member was created'
        assert response.body['member']['name'] == "Vitor Guirão MPNTM"
        assert response.body['member']['email_dev'] == "vsoller.devmaua@gmail.com"
        assert response.body['member']['email'] == "vsoller@airubio.com"
        assert response.body['member']['ra'] == "21017310"
        assert response.body['member']['role'] == ROLE.DIRECTOR
        assert response.body['member']['stack'] == STACK.INFRA
        assert response.body['member']['year'] == 1
        assert response.body['member']['cellphone'] == "11991758098"
        assert response.body['member']['course'] == COURSE.ECA
        assert response.body['member']['hired_date'] == 1614567601000
        assert response.body['member']['active'] == ACTIVE.ACTIVE
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
        
    def test_create_action_controller_name_entity_error(self):
            
        repo = MemberRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':234,
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
        assert response.body == 'Field name is not valid'
            
    def test_create_action_controller_missing_title(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'description':'Apenas um teste',
            'story_id': 100,
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field title is missing'
        
    def test_create_action_controller_missing_end_date(self):
                
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end_date is missing'
            
    def test_create_action_controller_missing_project_code(self):
                    
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field project_code is missing'
        
    def test_create_action_controller_missing_associated_members_ra(self):
                            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
    
    def test_create_action_controller_missing_end_date(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end_date is missing'
        
    def test_create_action_controller_end_date_entity_error(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date':'2h',
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end_date is not valid'
    
    def test_create_action_controller_start_and_end_date_entity_error(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634533200000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634526000000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field duration is not valid'
    
    def test_create_action_controller_missing_duration(self):
                
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field duration is missing'
        
    def test_create_action_controller_duration_entity_error(self):
                
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : '2h',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field duration is not valid'
        
    def test_create_action_controller_duration_too_big(self):
                    
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 10800000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field duration is not valid'
        
    def test_create_action_controller_stack_tags_not_list(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':'BACKEND',
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field stack_tags is not valid'
    
    def test_create_action_controller_stack_tags_is_none(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':None,
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field stack_tags is not valid'
        
    def test_create_action_controller_stack_tags_is_not_valid(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND','TESTE'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field stack_tags is not valid'
    
    def test_create_action_controller_action_type_tag_is_none(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':None
        })
        
        response = controller(request)
        assert response.body == 'Field action_type_tag is not valid'
        assert response.status_code == 400

    def test_create_action_controller_action_type_tag_is_not_valid(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'TESTE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_type_tag is not valid'

    def test_create_action_controller_duplicated_associated_members_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
        'owner_ra':'17033730',
        'start_date':1634526000000,
        'action_id':'82fc',
        'story_id': 100,
        'title':'Teste',
        'description':'Apenas um teste',
        'end_date' : 1634533200000,
        'duration' : 7200000,
        'project_code':'MF',
        'associated_members_ra':['19017310','19017310'],
        'stack_tags':['BACKEND'],
        'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field associated_members_ra is not valid'

    def test_create_action_controller_story_id_entity_error(self):
            
            repo = ActionRepositoryMock()
            usecase = CreateActionUsecase(repo=repo)
            controller = CreateActionController(usecase=usecase)
            request = HttpRequest(body={
                'owner_ra':'17033730',
                'start_date':1634526000000,

                'story_id':'100',
                'title':'Teste',
                'end_date' : 1634533200000,
                'duration' : 7200000,
                'project_code':'MF',
                'associated_members_ra':['19017310'],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            })
            
            response = controller(request)
            assert response.status_code == 400
            assert response.body == 'Field story_id is not valid'
            
    def test_create_action_controller_invalid_owner_ra(self):
            
            repo = ActionRepositoryMock()
            usecase = CreateActionUsecase(repo=repo)
            controller = CreateActionController(usecase=usecase)
            request = HttpRequest(body={
                'owner_ra':'3 21 18 9 15 19 15',
                'start_date':1634526000000,
                'story_id': 100,
                'title':'Teste',
                'end_date' : 1634533200000,
                'duration' : 7200000,
                'project_code':'MF',
                'associated_members_ra':['19017310'],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            })
            
            response = controller(request)
            assert response.status_code == 400
            assert response.body == 'Field owner_ra is not valid'
            
    def test_create_action_controller_invalid_associated_ra(self):
            
            repo = ActionRepositoryMock()
            usecase = CreateActionUsecase(repo=repo)
            controller = CreateActionController(usecase=usecase)
            request = HttpRequest(body={
                'owner_ra':'17033730',
                'start_date':1634526000000,
                'story_id': 100,
                'title':'Teste',
                'end_date' : 1634533200000,
                'duration' : 7200000,
                'project_code':'MF',
                'associated_members_ra':['3 21 18 9 15 19 15'],
                'stack_tags':['BACKEND'],
                'action_type_tag':'CODE'
            })
            
            response = controller(request)
            assert response.status_code == 400
            assert response.body == 'Field associated_members_ra is not valid'