import pytest
from src.modules.update_project.app.update_project_controller import UpdateProjectController
from src.modules.update_project.app.update_project_usecase import UpdateProjectUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class TestUpdateProjectController:

    def test_update_project_controller(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                'code': 'PT',
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_RA': '22456178',
                'new_scrum_RA': '20005632',
                'new_photos': ['new_photos']
            }
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body['project']['code'] == 'PT'
        assert response.body['project']['name'] == 'Portfolio'
        assert response.body['project']['description'] == 'Projeto do site portfolio'
        assert response.body['project']['po_RA'] == '22456178'
        assert response.body['project']['scrum_RA'] == '20005632'
        assert response.body['project']['photos'] == ['new_photos']

    def test_update_project_controller_missing_code(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_RA': '22456178',
                'new_scrum_RA': '20005632',
                'new_photos': ['new_photos']
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'

    def test_update_project_controller_project_not_found(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                'code': 'RR',
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_RA': '22456178',
                'new_scrum_RA': '20005632',
                'new_photos': ['new_photos']
            }
        )

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for project'

    def test_update_project_controller_code_not_valid(self):
        repo = ActionRepositoryMock()
        usecase = UpdateProjectUsecase(repo)
        controller = UpdateProjectController(usecase)

        request = HttpRequest(
            body={
                'code': 25,
                'new_name': 'Portfolio',
                'new_description': 'Projeto do site portfolio',
                'new_po_RA': '22456178',
                'new_scrum_RA': '20005632',
                'new_photos': ['new_photos']
            }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'