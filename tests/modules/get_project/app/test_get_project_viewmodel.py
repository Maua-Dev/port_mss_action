from src.modules.get_project.app.get_project_usecase import GetProjectUsecase
from src.modules.get_project.app.get_project_viewmodel import GetProjectViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetProjectViewmodel:
    def test_get_project_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetProjectUsecase(repo=repo)
        project = usecase(code='MF')

        viewmodel = GetProjectViewmodel(
            project=project[0], members=project[1]).to_dict()

        expected = {
            'project': {
                'code': 'MF',
                'name': 'Maua Food',
                'description': 'É um aplicativo #foramoleza',
                'po_RA': '21017310',
                'scrum_RA': '21010757',
                'start_date': 1634576165000,
                'photos': [
                    'https://i.imgur.com/gHoRKJU.png'
                ]
            },
            'members': [
                {
                    'name': 'Vitor Guirão MPNTM',
                    'email_dev': 'vsoller.devmaua@gmail.com',
                    'email': 'vsoller@airubio.com',
                    'ra': '21017310',
                    'role': 'DIRECTOR',
                    'stack': 'INFRA',
                    'year': 1,
                    'cellphone': '11991758098',
                    'course': 'ECA',
                    'hired_date': 1634576165000,
                    'deactivated_date': None,
                    'active': 'ACTIVE',
                    'projects': ['MF']
                },
                {
                    'name': 'Joao Branco',
                    'email_dev': 'jbranco.devmaua@gmail.com',
                    'email': 'jbranco@gmail.com',
                    'ra': '21010757',
                    'role': 'HEAD',
                    'stack': 'BACKEND',
                    'year': 3,
                    'cellphone': '11991152348',
                    'course': 'ECM',
                    'hired_date': 1634921765000,
                    'deactivated_date': None,
                    'active': 'ACTIVE',
                    'projects': ['MF','PT','SF']
                },
                {
                    'name': 'Little Ronald',
                    'email_dev': 'lronald.devmaua@gmail.com',
                    'email': 'lronald@gmail.com',
                    'ra': '10017310',
                    'role': 'DIRECTOR',
                    'stack': 'FRONTEND',
                    'year': 6,
                    'cellphone': '11991759998',
                    'course': 'ECM',
                    'hired_date': 1614567601000,
                    'deactivated_date': None,
                    'active': 'ACTIVE',
                    'projects': ['MF','PT','SF','SM']
                }
            ],
            'message': 'the project was retrieved'
        }

        assert viewmodel == expected