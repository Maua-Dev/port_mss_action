from src.modules.get_all_projects.app.get_all_projects_usecase import GetAllProjectsUsecase
from src.modules.get_all_projects.app.get_all_projects_viewmodel import GetAllProjectsViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetAllProjectsViewmodel:
    def test_get_all_projects_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetAllProjectsUsecase(repo)
        projects = usecase()

        viewmodel = GetAllProjectsViewmodel(projects).to_dict()

        expected = {
            'projects': [
                {
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
                    }
                },
                {
                    'project': {
                        'code': 'PT',
                        'name': 'Portfólio',
                        'description': 'É um site',
                        'po_RA': '22011020',
                        'scrum_RA': '21010757',
                        'start_date': 1673535600000,
                        'photos': [
                            'https://i.imgur.com/gHoRKJU.png'
                        ]
                    }
                },
                {
                    'project': {
                        'code': 'SF',
                        'name': 'Selfie Mauá',
                        'description': 'Aplicativo para reconhecimento facial',
                        'po_RA': '22931270',
                        'scrum_RA': '21020532',
                        'start_date': 1686754800000,
                        'photos': [

                        ]
                    }
                },
                {
                    'project': {
                        'code': 'SM',
                        'name': 'SMILE',
                        'description': 'Site do evento SMILE',
                        'po_RA': '15014025',
                        'scrum_RA': '21010757',
                        'start_date': 1639321200000,
                        'photos': [

                        ]
                    }
                },
                {
                    'project': {
                        'code': 'GM',
                        'name': 'Gameficação',
                        'description': 'Projeto para organização dos membros do DEV',
                        'po_RA': '22084120',
                        'scrum_RA': '22015940',
                        'start_date': 1672585200000,
                        'photos': [

                        ]
                    }
                }
            ],
            'message': 'the projects were retrieved'
        }
        
        assert viewmodel == expected