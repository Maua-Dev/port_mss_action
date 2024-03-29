from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.modules.get_all_members.app.get_all_members_viewmodel import GetAllMembersViewmodel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

class Test_GetAllMembersViewModel:

    def test_get_all_members_viewmodel(self):
        repo = MemberRepositoryMock()
        usecase = GetAllMembersUsecase(repo=repo)
        members = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3")

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
                        'active': 'ACTIVE',
                        'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
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
                        'active': 'ACTIVE',
                        'user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
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
                        'active': 'FREEZE',
                        'user_id': "76h35dg4-h76v-1875-987hn-h67gfv45Gt4"
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
                        'active': 'ACTIVE',
                        'user_id': "6f5g4h7J-876j-0098-123hb-hgb567fy4hb"
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
                        'active': 'DISCONNECTED',
                        'user_id': "6574hgyt-785n-9134-18gn4-7gh5uvn36cG"
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
                        'active': 'ACTIVE',
                        'user_id': "7gh5yf5H-857H-1234-75hng-94832hvng1s"
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
                        'active': 'FREEZE',
                        'user_id': "7465hvnb-143g-1675-86HnG-75hgnFbcg36"
                        }
                },
                {
                    'member': {
                        'name': 'Henrique Gustavo de Souza',
                        'email_dev': 'hsouza.devmaua@gmail.com',
                        'email': 'hsouza@gmail.com',
                        'ra': '22015320',
                        'role': 'DEV',
                        'stack': 'UX_UI',
                        'year': 1,
                        'cellphone': '11991123498',
                        'course': 'ECM',
                        'hired_date': 1672592165000,
                        'deactivated_date': None,
                        'active': 'ACTIVE',
                        'user_id': "75648hbr-184n-1985-91han-7ghn4HgF182"
                        }
                },
                {
                    'member': {
                        'name': 'Joao Pedro Soares',
                        'email_dev': 'jp.devmaua@gmail.com',
                        'email': 'jp@gmail.com',
                        'ra': '21004102',
                        'role': 'DEV',
                        'stack': 'UX_UI',
                        'year': 1,
                        'cellphone': '11991123498',
                        'course': 'ECM',
                        'hired_date': 1672592165000,
                        'deactivated_date': None,
                        'active': 'ACTIVE',
                        'user_id': "9183jBnh-997H-1010-10god-914gHy46tBh"
                        }
                }
            ],
            'message' : 'the members were retrieved'
        }

        assert viewmodel == expected
                
                        