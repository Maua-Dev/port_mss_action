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
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the action was created'
        assert response.body['action']['owner_ra'] == '17033730'
        assert response.body['action']['start_time'] == 1634526000000
        assert response.body['action']['action_id'] == '82fc'
        assert response.body['action']['title'] == 'Teste'
        assert response.body['action']['end_time'] == 1634533200000
        assert response.body['action']['project_code'] == 'MF'
        assert response.body['action']['associated_members_ra'] == ['19017310']
        assert response.body['action']['stack_tags'] == ['BACKEND']
        assert response.body['action']['action_type_tags'] == ['CODE']
    
    def test_create_action_controller_missing_action_id(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_id is missing'
    
    def test_create_action_controller_missing_owner_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field owner_ra is missing'
        
    def test_create_action_controller_missing_start_time(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_time is missing'
        
    def test_create_action_controller_start_time_entity_error(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':'1634526000000',
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_time is not valid'
            
    def test_create_action_controller_missing_title(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field title is missing'
        
    def test_create_action_controller_missing_end_time(self):
                
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end_time is missing'
            
    def test_create_action_controller_missing_project_code(self):
                    
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
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
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 201
    
    def test_create_action_controller_missing_end_time(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end_time is missing'
        
    def test_create_action_controller_end_time_entity_error(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time':'2h',
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field end_time is not valid'
    
    def test_create_action_controller_start_and_end_time_entity_error(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634533200000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634526000000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_time and end_time is not valid'
    
    def test_create_action_controller_missing_duration(self):
                
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
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
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : '2h',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
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
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 10800000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
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
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':'BACKEND',
            'action_type_tags':['CODE']
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
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':None,
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['action']['stack_tags'] == []
        
    def test_create_action_controller_stack_tags_is_not_valid(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND','TESTE'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field stack_tags is not valid'
    
    def test_create_action_controller_action_type_tags_not_list(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_type_tags is not valid'
        
    def test_create_action_controller_action_type_tags_is_none(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':None
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['action']['action_type_tags'] == []
        
    def test_create_action_controller_action_type_tags_is_not_valid(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'82fc',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE','TESTE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_type_tags is not valid'
        
    def test_create_action_controller_duplicated_action_id(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'start_time':1634526000000,
            'action_id':'9fc2',
            'title':'Teste',
            'end_time' : 1634533200000,
            'duration' : 7200000,
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'The item alredy exists for this action_id'
        
    def test_create_action_controller_ra_not_found(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
        'owner_ra':'12345678',
        'start_time':1634526000000,
        'action_id':'82fc',
        'title':'Teste',
        'end_time' : 1634533200000,
        'duration' : 7200000,
        'project_code':'MF',
        'associated_members_ra':['19017310'],
        'stack_tags':['BACKEND'],
        'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 404
        assert response.body == 'No items found for owner_ra'
        
    def test_create_action_controller_associated_members_ra_not_found(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
        'owner_ra':'17033730',
        'start_time':1634526000000,
        'action_id':'82fc',
        'title':'Teste',
        'end_time' : 1634533200000,
        'duration' : 7200000,
        'project_code':'MF',
        'associated_members_ra':['12345678'],
        'stack_tags':['BACKEND'],
        'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 404
        assert response.body == 'No items found for associated_members_ra'

    def test_create_action_controller_duplicated_associated_members_ra(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
        'owner_ra':'17033730',
        'start_time':1634526000000,
        'action_id':'82fc',
        'title':'Teste',
        'end_time' : 1634533200000,
        'duration' : 7200000,
        'project_code':'MF',
        'associated_members_ra':['19017310','19017310'],
        'stack_tags':['BACKEND'],
        'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field associated_members_ra is not valid'