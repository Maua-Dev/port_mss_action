from src.modules.delete_project.app.delete_project_controller import DeleteProjectController
from src.modules.delete_project.app.delete_project_usecase import DeleteProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_DeleteProjectController:
    def test_delete_project_controller(self):
        
        repo = ActionRepositoryMock()
        usecase = DeleteProjectUsecase(repo)
        controller = DeleteProjectController(usecase)
        request = HttpRequest(body={
            'code': 'MF'
        })
        response = controller(request)
        assert response.status_code == 200
        assert response.body["message"] == "the project was deleted"
        assert response.body["project"]["code"] == "MF"
        assert response.body["project"]["name"] == "Maua Food"
        assert response.body["project"]["description"] == "É um aplicativo #foramoleza"
        assert response.body["project"]["po_RA"] == "21017310"
        assert response.body["project"]["scrum_RA"] == "21010757"
        assert response.body["project"]["start_date"] == 1634576165000
        assert response.body["project"]["photos"] == ["https://i.imgur.com/gHoRKJU.png"]
        
    def test_delete_project_controller_missing_code(self):
        
        repo = ActionRepositoryMock()
        usecase = DeleteProjectUsecase(repo)
        controller = DeleteProjectController(usecase)
        request = HttpRequest(body={})
        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field code is missing"
        
    def test_delete_project_controller_invalid_code(self):
            
            repo = ActionRepositoryMock()
            usecase = DeleteProjectUsecase(repo)
            controller = DeleteProjectController(usecase)
            request = HttpRequest(body={
                'code': 'M'
            })
            response = controller(request)
            assert response.status_code == 400
            assert response.body == "Field code is not valid"
            
    def test_delete_project_controller_project_not_found(self):
                
                repo = ActionRepositoryMock()
                usecase = DeleteProjectUsecase(repo)
                controller = DeleteProjectController(usecase)
                request = HttpRequest(body={
                    'code': 'LT'
                })
                response = controller(request)
                assert response.status_code == 404
                assert response.body == "No items found for project"