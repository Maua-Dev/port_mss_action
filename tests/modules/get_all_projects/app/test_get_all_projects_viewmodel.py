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
                    },
                    'members':[
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
                            'projects': [
                                'MF'
                            ]
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF'
                            ]
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF',
                                'SM'
                            ]
                        }
                    ]
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
                    },
                    'members':[
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF'
                            ]
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF',
                                'SM'
                            ]
                        }
                    ]
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
                    },
                    'members':[
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF'
                            ]
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF',
                                'SM'
                            ]
                        },
                        {
                            'name': 'Rubicks Cube',
                            'email_dev': 'rcube.devmaua@gmail.com',
                            'email': 'rubikscube@gmail.com',
                            'ra': '19017311',
                            'role': 'DEV',
                            'stack': 'BACKEND',
                            'year': 3,
                            'cellphone': '11911758098',
                            'course': 'ECM',
                            'hired_date': 1640192165000,
                            'deactivated_date': None,
                            'active': 'ACTIVE',
                            'projects': [
                                'SM',
                                'SF'
                            ]
                        }
                    ]
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
                    },
                    'members':[
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
                            'projects': [
                                'MF',
                                'PT',
                                'SF',
                                'SM'
                            ]
                        },
                        {
                            'name': 'Rubicks Cube',
                            'email_dev': 'rcube.devmaua@gmail.com',
                            'email': 'rubikscube@gmail.com',
                            'ra': '19017311',
                            'role': 'DEV',
                            'stack': 'BACKEND',
                            'year': 3,
                            'cellphone': '11911758098',
                            'course': 'ECM',
                            'hired_date': 1640192165000,
                            'deactivated_date': None,
                            'active': 'ACTIVE',
                            'projects': [
                                'SM',
                                'SF'
                            ]
                        }
                    ]
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
                    },
                    'members':[

                    ]
                }
            ],
            'message': 'the projects were retrieved'
        }
        
        assert viewmodel == expected