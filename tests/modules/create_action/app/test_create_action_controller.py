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
            'date':1634526000,
            'action_id':'82fc',
            'title':'Teste',
            'duration':'02:00:00',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the action was created'
        assert response.body['action']['owner_ra'] == '17033730'
        assert response.body['action']['date'] == 1634526000
        assert response.body['action']['action_id'] == '82fc'
        assert response.body['action']['title'] == 'Teste'
        assert response.body['action']['duration'] == '02:00:00'
        assert response.body['action']['project_code'] == 'MF'
        assert response.body['action']['associated_members_ra'] == ['19017310']
        assert response.body['action']['stack_tags'] == ['BACKEND']
        assert response.body['action']['action_type_tags'] == ['CODE']
    
    def test_create_action_controller_missing_parameters(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'date':1634526000,
            'title':'Teste',
            'duration':'02:00:00',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_id is missing'
    
    def test_create_action_controller_duration_entity_error(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'date':1634526000,
            'action_id':'82fc',
            'title':'Teste',
            'duration':'2h',
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
            'date':1634526000,
            'action_id':'82fc',
            'title':'Teste',
            'duration':'02:00:00',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':'BACKEND',
            'action_type_tags':['CODE']
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field stack_tags is not valid'
        
    def test_create_action_controller_stack_tags_not_valid(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'date':1634526000,
            'action_id':'82fc',
            'title':'Teste',
            'duration':'02:00:00',
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
            'date':1634526000,
            'action_id':'82fc',
            'title':'Teste',
            'duration':'02:00:00',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':'CODE'
        })
        
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field action_type_tags is not valid'
        
    def test_create_action_controller_action_type_tags_not_valid(self):
            
            repo = ActionRepositoryMock()
            usecase = CreateActionUsecase(repo=repo)
            controller = CreateActionController(usecase=usecase)
            request = HttpRequest(body={
                'owner_ra':'17033730',
                'date':1634526000,
                'action_id':'82fc',
                'title':'Teste',
                'duration':'02:00:00',
                'project_code':'MF',
                'associated_members_ra':['19017310'],
                'stack_tags':['BACKEND'],
                'action_type_tags':['CODE','TESTE']
            })
            
            response = controller(request)
            assert response.status_code == 400
            assert response.body == 'Field action_type_tags is not valid'
        
    def test_create_action_controller_duplicated_id(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateActionUsecase(repo=repo)
        controller = CreateActionController(usecase=usecase)
        request = HttpRequest(body={
            'owner_ra':'17033730',
            'date':1634526000,
            'action_id':'9fc2',
            'title':'Teste',
            'duration':'02:00:00',
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
            'date':1634526000,
            'action_id':'82fc',
            'title':'Teste',
            'duration':'02:00:00',
            'project_code':'MF',
            'associated_members_ra':['19017310'],
            'stack_tags':['BACKEND'],
            'action_type_tags':['CODE']
        })
            
            response = controller(request)
            assert response.status_code == 404
            assert response.body == 'No items found for owner_ra'