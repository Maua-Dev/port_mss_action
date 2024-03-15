from src.modules.update_project.app.update_project_viewmodel import UpdateProjectViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class TestUpdateProjectViewmodel:
    def test_update_project_viewmodel(self):
        repo = ActionRepositoryMock()
        viewmodel = UpdateProjectViewmodel(repo.projects[1])

        expected = {
            'message': 'the project was updated',
            'project': {
                'code': 'PT',
                'name': 'Portfólio',
                'description': 'É um site',
                'po_user_id': '22011020',
                'scrum_user_id': '21010757',
                'start_date': 1673535600000,
                'photos': ['https://i.imgur.com/gHoRKJU.png']
            }
        }

        assert viewmodel.to_dict() == expected