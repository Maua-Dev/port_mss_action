from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.modules.get_project.app.get_project_viewmodel import GetProjectViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetProjectViewmodel:
    def test_get_project_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        project = usecase(code='MF')

        viewmodel = GetProjectViewmodel(
            project=project).to_dict()

        expected = {
            'project': {
                'code': 'MF',
                'name': 'Maua Food',
                'description': 'É um aplicativo #foramoleza',
                'po_user_id': '21017310',
                'scrum_user_id': '21010757',
                'start_date': 1634576165000,
                'members': ['10017310','21010757','21017310'],
                'photos': [
                    'https://i.imgur.com/gHoRKJU.png'
                ]
            },
            'message': 'the project was retrieved'
        }

        assert viewmodel == expected