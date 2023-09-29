from src.modules.create_action.app.create_action_controller import CreateActionController
from src.modules.create_action.app.create_action_usecase import CreateActionUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateActionController:
    def test_create_action_controller(self):
        
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
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the action was created'
        assert response.body['action']['owner_ra'] == '17033730'
        assert response.body['action']['start_date'] == 1634526000000
        assert response.body['action']['story_id'] == 100
        assert response.body['action']['title'] == 'Teste'
        assert response.body['action']['description'] == 'Apenas um teste'
        assert response.body['action']['end_date'] == 1634533200000
        assert response.body['action']['project_code'] == 'MF'
        assert response.body['action']['associated_members_ra'] == ['19017310']
        assert response.body['action']['stack_tags'] == ['BACKEND']
        assert response.body['action']['action_type_tag'] == 'CODE'
    
    def test_create_action_controller_missing_owner_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'start_date':1634526000000,
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field owner_ra is missing'
        
    def test_create_action_controller_missing_start_date(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_date is missing'
        
    def test_create_action_controller_start_date_entity_error(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_date':'1634526000000',
            'story_id': 100,
            'title':'Teste',
            'description':'Apenas um teste',
            'end_date' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tag':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_date is not valid'
            
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