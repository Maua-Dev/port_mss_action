from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.modules.get_all_members.app.get_all_members_viewmodel import GetAllMembersViewmodel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

class Test_GetAllMembersViewModel:

    def test_get_all_members_viewmodel(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
        members = usecase("93bc6ada-c0d1-7054-66ab-e17414c48ae3", start_date= 1624576165000, end_date= 1690046000000)

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
                        'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                        'hours_worked': 143960000000
                        
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
                        'user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                        'hours_worked': 104090000000
                        }
                },
                {
                    'member': {
                        'name': 'Luigi Televisão',
                        'email_dev': 'ltelevisao.devmaua@gmail.com',
                        'email': 'lgtv@gmail.com',
                        'ra': '22017310',
                        'role': 'DEV',
                        'stack': 'BACKEND',
                        'year': 2,
                        'cellphone': '11991758228',
                        'course': 'CIC',
                        'hired_date': 1640192165000,
                        'deactivated_date': None,
                        'active': 'FREEZE',
                        'user_id': "76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                        'hours_worked': 72430000000
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
                        'user_id': "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                        'hours_worked': 160010000000
                        }
                },
                {
                    'member': {
                        'name': 'Marcos Pereira Neto',
                        'email_dev': 'mneto.devmaua@gmail.com',
                        'email': 'mneto@gmail.com',
                        'ra': '19017310',
                        'role': 'PO',
                        'stack': 'BUSINESS',
                        'year': 4,  
                        'cellphone': '11991753208',
                        'course': 'EMC',
                        'hired_date': 1614567601000,
                        'deactivated_date': None,
                        'active': 'DISCONNECTED',
                        'user_id': "6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                        'hours_worked': 184430000000
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
                        'user_id': "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                        'hours_worked': 107350000000
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
                        'user_id': "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                        'hours_worked': 79580000000
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
                        'user_id': "75648hbr-184n-1985-91han-7ghn4HgF182",
                        'hours_worked': 119700000000
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
                        'user_id': "9183jBnh-997H-1010-10god-914gHy46tBh",
                        'hours_worked': 0
                        }
                },
                {
                    'member': {
                        'name' : "Fernandao Presidas",
                        'email_dev' : "fernandinho.devmaua@gmail.com",
                        'email' : "fernandao@gmail.com",
                        'ra' : "22014322",
                        'role' : 'PO',
                        'stack' : 'BUSINESS',
                        'year' : 3,
                        'cellphone' : "11991123498",
                        'course' : 'EPM',
                        'hired_date' : 1640192165000,
                        'active' : 'ACTIVE',
                        'deactivated_date' : None,
                        'user_id' : "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                        'hours_worked' : 0
                        }
                },
                {
                    'member' : {
                        'name' : "Carlinhos Miau",
                        'email_dev' : "carlinhos.devmaua@gmail.com",
                        'email' : "carlinhosmiau@gmail.com",
                        'ra' : "23024211",
                        'role' : 'DEV',
                        'stack' : 'BACKEND',
                        'year' : 3,
                        'cellphone' : "11998472663",
                        'course' : 'ECM',
                        'hired_date' : 1640192165000,
                        'active' : 'ON_HOLD',
                        'deactivated_date' : None,
                        'user_id' : "3b07232f-4f65-42c6-b005-242550b8b8dc",
                        'hours_worked' : 0
                        }
                }
            ],
            'message' : 'the members were retrieved'
        }

        assert viewmodel == expected
        
        
    def test_get_all_members_viewmodel_no_start_and_end_date(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        usecase = GetAllMembersUsecase(memberrepo=memberrepo, actionrepo=actionrepo)
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
                        'user_id': "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                        'hours_worked': 0
                        
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
                        'user_id': "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                        'hours_worked': 0
                        }
                },
                {
                    'member': {
                        'name': 'Luigi Televisão',
                        'email_dev': 'ltelevisao.devmaua@gmail.com',
                        'email': 'lgtv@gmail.com',
                        'ra': '22017310',
                        'role': 'DEV',
                        'stack': 'BACKEND',
                        'year': 2,
                        'cellphone': '11991758228',
                        'course': 'CIC',
                        'hired_date': 1640192165000,
                        'deactivated_date': None,
                        'active': 'FREEZE',
                        'user_id': "76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                        'hours_worked': 0
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
                        'user_id': "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                        'hours_worked': 0
                        }
                },
                {
                    'member': {
                        'name': 'Marcos Pereira Neto',
                        'email_dev': 'mneto.devmaua@gmail.com',
                        'email': 'mneto@gmail.com',
                        'ra': '19017310',
                        'role': 'PO',
                        'stack': 'BUSINESS',
                        'year': 4,  
                        'cellphone': '11991753208',
                        'course': 'EMC',
                        'hired_date': 1614567601000,
                        'deactivated_date': None,
                        'active': 'DISCONNECTED',
                        'user_id': "6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                        'hours_worked': 0
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
                        'user_id': "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                        'hours_worked': 0
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
                        'user_id': "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                        'hours_worked': 0
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
                        'user_id': "75648hbr-184n-1985-91han-7ghn4HgF182",
                        'hours_worked': 0
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
                        'user_id': "9183jBnh-997H-1010-10god-914gHy46tBh",
                        'hours_worked': 0
                        }
                },
                {
                    'member': {
                        'name' : "Fernandao Presidas",
                        'email_dev' : "fernandinho.devmaua@gmail.com",
                        'email' : "fernandao@gmail.com",
                        'ra' : "22014322",
                        'role' : 'PO',
                        'stack' : 'BUSINESS',
                        'year' : 3,
                        'cellphone' : "11991123498",
                        'course' : 'EPM',
                        'hired_date' : 1640192165000,
                        'active' : 'ACTIVE',
                        'deactivated_date' : None,
                        'user_id' : "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                        'hours_worked' : 0
                        }
                },
                {
                    'member' : {
                        'name' : "Carlinhos Miau",
                        'email_dev' : "carlinhos.devmaua@gmail.com",
                        'email' : "carlinhosmiau@gmail.com",
                        'ra' : "23024211",
                        'role' : 'DEV',
                        'stack' : 'BACKEND',
                        'year' : 3,
                        'cellphone' : "11998472663",
                        'course' : 'ECM',
                        'hired_date' : 1640192165000,
                        'active' : 'ON_HOLD',
                        'deactivated_date' : None,
                        'user_id' : "3b07232f-4f65-42c6-b005-242550b8b8dc",
                        'hours_worked' : 0
                        }
                }
            ],
            'message' : 'the members were retrieved'
        }

        assert viewmodel == expected
    