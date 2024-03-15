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
                        'po_user_id': '21017310',
                        'scrum_user_id': '21010757',
                        'start_date': 1634576165000,
                        'members': ['10017310','21010757','21017310'],
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
                        'po_user_id': '22011020',
                        'scrum_user_id': '21010757',
                        'start_date': 1673535600000,
                        'members': ['10017310', '21010757', '22011020'],
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
                        'po_user_id': '22931270',
                        'scrum_user_id': '21020532',
                        'start_date': 1686754800000,
                        'members':['10017310', '19017311', '21010757', '21020532', '22931270'],
                        'photos': [

                        ]
                    }
                },
                {
                    'project': {
                        'code': 'SM',
                        'name': 'SMILE',
                        'description': 'Site do evento SMILE',
                        'po_user_id': '15014025',
                        'scrum_user_id': '21010757',
                        'start_date': 1639321200000,
                        'members': ['10017310', '15014025', '19017311', '21010757'],
                        'photos': [

                        ]
                    }
                },
                {
                    'project': {
                        'code': 'GM',
                        'name': 'Gameficação',
                        'description': 'Projeto para organização dos membros do DEV',
                        'po_user_id': '22084120',
                        'scrum_user_id': '22015940',
                        'start_date': 1672585200000,
                        'members': ['22015940', '22084120'],
                        'photos': [

                        ]
                    }
                }
            ],
            'message': 'the projects were retrieved'
        }
        
        assert viewmodel == expected