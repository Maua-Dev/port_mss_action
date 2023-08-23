from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.modules.get_all_members.app.get_all_members_viewmodel import GetAllMembersViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetAllMembersViewModel:

    def test_get_all_members_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        members = usecase()

        viewmodel = GetAllMembersViewmodel(members).to_dict()

        expected = {
            'members': [
                {
                    'member': {
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
                        'active': 'ACTIVE'
                        }
                },
                {
                    'member': {
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
                        'active': 'ACTIVE'
                        }
                },
                {
                    'member': {
                        'name': 'Luigi Televisão',
                        'email_dev': 'ltelevisao.devmaua@gmail.com',
                        'email': 'lgtv@gmail.com',
                        'ra': '22017310',
                        'role': 'DEV',
                        'stack': 'DATA_SCIENCE',
                        'year': 2,
                        'cellphone': '11991758228',
                        'course': 'CIC',
                        'hired_date': 1640192165000,
                        'deactivated_date': None,
                        'active': 'FREEZE'
                        }
                },
                {
                    'member': {
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
                        'active': 'ACTIVE'
                        }
                },
                {
                    'member': {
                        'name': 'Marcos Pereira Neto',
                        'email_dev': 'mneto.devmaua@gmail.com',
                        'email': 'mneto@gmail.com',
                        'ra': '19017310',
                        'role': 'PO',
                        'stack': 'PO',
                        'year': 4,  
                        'cellphone': '11991753208',
                        'course': 'EMC',
                        'hired_date': 1614567601000,
                        'deactivated_date': None,
                        'active': 'DISCONNECTED'
                        }               
                },
                {
                    'member': {
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
                        'active': 'ACTIVE'
                        }
                },
                {
                    'member': {
                        'name': 'Django Fett',
                        'email_dev': 'dfett.devmaua@gmail.com',
                        'email': 'djangofett@starwars.com',
                        'ra': '17033730',
                        'role': 'INTERNAL',
                        'stack': 'INTERNAL',
                        'year': 2,
                        'cellphone': '11915758098',
                        'course': 'ECA',
                        'hired_date': 1609606565000,
                        'deactivated_date': None,
                        'active': 'FREEZE'
                        }
                },
                {
                    'member': {
                        'name': 'Henrique Gustavo de Souza',
                        'email_dev': 'hsouza.devmaua@gmail.com',
                        'email': 'hsouza@gmail.com',
                        'ra': '23017310',
                        'role': 'DEV',
                        'stack': 'UX_UI',
                        'year': 1,
                        'cellphone': '11991123498',
                        'course': 'ECM',
                        'hired_date': 1672592165000,
                        'deactivated_date': None,
                        'active': 'ACTIVE'
                        }
                }
            ],
            'message' : 'the members were retrieved'
        }

        assert viewmodel == expected
                
                        