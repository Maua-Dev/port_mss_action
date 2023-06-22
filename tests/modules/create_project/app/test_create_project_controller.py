from src.modules.create_project.app.create_project_controller import CreateProjectController
from src.modules.create_project.app.create_project_usecase import CreateProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_CreateProjectController:
    def test_create_project_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_RA':'21021031',
            'scrum_RA':'17033730',
            'start_date':1649955600000,
            'photos':['https://i.imgur.com/7QF7uCk.png']
        })
        response = controller(request)
        assert response.status_code == 201
        assert response.body['message'] == 'the project was created'
        assert response.body['project']['code'] == 'DM'
        assert response.body['project']['name'] == 'DevMedias'
        assert response.body['project']['description'] == 'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano'
        assert response.body['project']['po_RA'] == '21021031'
        assert response.body['project']['scrum_RA'] == '17033730'
        assert response.body['project']['start_date'] == 1649955600000
        assert response.body['project']['photos'] == ['https://i.imgur.com/7QF7uCk.png']
        
    def test_create_project_controller_missing_photos(self):
            
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_RA':'21021031',
            'scrum_RA':'17033730',
            'start_date':1649955600000
        })
        response = controller(request)
        assert response.status_code == 201
        assert response.body['project']['photos'] == []
        
    def test_create_project_controller_missing_code(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_RA':'21021031',
            'scrum_RA':'17033730',
            'start_date':1649955600000
        })
        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field code is missing'
        
    def test_create_project_controller_missing_name(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_RA':'21021031',
            'scrum_RA':'17033730',
            'start_date':1649955600000
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field name is missing'
        
    def test_create_project_controller_missing_description(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'name':'DevMedias',
            'po_RA':'21021031',
            'scrum_RA':'17033730',
            'start_date':1649955600000
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field description is missing'
        
    def test_create_project_controller_missing_po_RA(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'scrum_RA':'17033730',
            'start_date':1649955600000
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field po_RA is missing'
        
    def test_create_project_controller_missing_scrum_RA(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_RA':'21021031',
            'start_date':1649955600000
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field scrum_RA is missing'
        
    def test_create_project_controller_missing_start_date(self):
        
        repo = ActionRepositoryMock()
        usecase = CreateProjectUsecase(repo=repo)
        controller = CreateProjectController(usecase=usecase)
        request = HttpRequest(body = {
            'code':'DM',
            'name':'DevMedias',
            'description':'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
            'po_RA':'21021031',
            'scrum_RA':'17033730'
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body == 'Field start_date is missing'