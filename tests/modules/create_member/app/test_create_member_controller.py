import pytest
from src.modules.create_member.app.create_member_controller import CreateMemberController
from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_CreateMemberController:
    def test_create_member_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 201
        assert response.body['message'] == "the member was created"
        assert response.body['member']['name'] == "Teste"
        assert response.body['member']['email'] == "teste.devmaua@gmail.com"
        assert response.body['member']['ra'] == "12345678"
        assert response.body['member']['role'] == "DEV"
        assert response.body['member']['stack'] == "BACKEND"
        assert response.body['member']['year'] == 2
        assert response.body['member']['cellphone'] == "11912345678"
        assert response.body['member']['course'] == "CIC"
        assert response.body['member']['hired_date'] == 1634526000
        assert response.body['member']['deactivated_date'] == None
        assert response.body['member']['active'] == "ACTIVE"
        assert response.body['member']['projects'][0]['code'] == "MF"
        assert response.body['member']['projects'][0]['name'] == "Maua Food"
        assert response.body['member']['projects'][0]['description'] == "É um aplicativo #foramoleza"
    
    def test_create_member_controller_missing_deactivated_date(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':None,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 201
        assert response.body['message'] == "the member was created"
        assert response.body['member']['deactivated_date'] == None
    
    def test_create_member_controller_missing_projects(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':None,
            'active':'ACTIVE',
            'projects':[],
        })
        
        response = controller(request=request)
        assert response.status_code == 201
        assert response.body['message'] == "the member was created"
        assert response.body['member']['projects'] == []
        
    def test_create_member_controller_missing_name(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':None,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field name is missing"
            
        
    def test_create_member_controller_missing_email(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':None,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field email is missing"
        
    def test_create_member_controller_invalid_email(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':None,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field email is not valid"
        
    def test_create_member_controller_missing_ra(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field ra is missing"
        
    def test_create_member_controller_invalid_ra(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12.34567-8',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field ra is not valid"
        
    def test_create_member_controller_duplicated_ra(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'21017310',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "The item alredy exists for this ra"
        
    def test_create_member_controller_missing_role(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field role is missing"
        
    def test_create_member_controller_invalid_role(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'desenvolvedor',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field role is not valid"
        
    def test_create_member_controller_missing_stack(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field stack is missing"
        
    def test_create_member_controller_invalid_stack(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'back-end',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field stack is not valid"
        
    def test_create_member_controller_missing_year(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field year is missing"
        
    def test_create_member_controller_invalid_year(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2022,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field year is not valid"
        
    def test_create_member_controller_missing_cellphone(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field cellphone is missing"
        
    def test_create_member_controller_missing_course(self): 
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field course is missing"
        
    def test_create_member_controller_invalid_course(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'Design',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field course is not valid"
        
    def test_create_member_controller_missing_hired_date(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field hired_date is missing"
        
    def test_create_member_controller_invalid_hired_date(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':'18/10/2021',
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field hired_date is not valid"
        
    def test_create_member_controller_invalid_deactivated_date(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':'18/10/2022',
            'active':'ACTIVE',
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field deactivated_date is not valid"
        
    def test_create_member_controller_missing_active(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field active is missing"

    def test_create_member_controller_invalid_active(self):
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':True,
            'projects':[
                {
                    'code':'MF',
                    'name':'Maua Food',
                    'description':'É um aplicativo #foramoleza'
                }
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field active is not valid"
    
    def test_create_member_controller_invalid_projects(self): 
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':1,
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field projects is not valid"
    
    def test_create_member_controller_invalid_project_items(self): 
        repo = ActionRepositoryMock()
        usecase = CreateMemberUsecase(repo=repo)
        controller = CreateMemberController(usecase=usecase)
        request = HttpRequest(body={
            'name':'Teste',
            'email':'teste.devmaua@gmail.com',
            'ra':'12345678',
            'role':'DEV',
            'stack':'BACKEND',
            'year':2,
            'cellphone':'11912345678',
            'course':'CIC',
            'hired_date':1634526000,
            'deactivated_date':1666062000,
            'active':'ACTIVE',
            'projects':[
                "MF"
            ],
        })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field projects is not valid"