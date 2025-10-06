from src.modules.get_all_members_admin.app.get_all_members_admin_controller import GetAllMembersAdminController
from src.modules.get_all_members_admin.app.get_all_members_admin_usecase import GetAllMembersAdminUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock

class Test_GetAllMembersAdminController:

    def test_get_all_members_controller(self):
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        strikerepo = StrikeRepositoryMock()
        usecase = GetAllMembersAdminUsecase(memberrepo=memberrepo, actionrepo=actionrepo, strikerepo=strikerepo)
        controller = GetAllMembersAdminController(usecase=usecase)
        
        request = HttpRequest(body={
            'requester_user': {
                "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
            },
            'start_date': 1624576165000,
            'end_date': 1690046000000
        })
        
        response = controller(request=request)
        expected_dict = {'members': [
    {'member': {'active': 'ACTIVE', 'cellphone': '11991758098', 'course': 'ECA', 'deactivated_date': None, 'email': 'vsoller@airubio.com', 'email_dev': 'vsoller.devmaua@gmail.com', 'hired_date': 1634576165000, 'hours_worked': 143960000000, 'name': 'Vitor Guirão MPNTM', 'photo': None, 'project': ['Maua Food', 'Portfólio', 'Selfie Mauá'], 'ra': '21017310', 'role': 'DIRECTOR', 'stack': 'INFRA', 'strikes': 0, 'strikes_allowed': 4, 'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3', 'year': 1}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11991152348', 'course': 'ECM', 'deactivated_date': None, 'email': 'jbranco@gmail.com', 'email_dev': 'jbranco.devmaua@gmail.com', 'hired_date': 1634921765000, 'hours_worked': 104090000000, 'name': 'Joao Branco', 'photo': None, 'project': ['Maua Food', 'Portfólio', 'Selfie Mauá', 'SMILE'], 'ra': '21010757', 'role': 'HEAD', 'stack': 'BACKEND', 'strikes': 0, 'strikes_allowed': 4, 'user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3', 'year': 3}},
    {'member': {'active': 'FREEZE', 'cellphone': '11991758228', 'course': 'CIC', 'deactivated_date': None, 'email': 'lgtv@gmail.com', 'email_dev': 'ltelevisao.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 72430000000, 'name': 'Luigi Televisão', 'photo': None, 'project': ['Gameficação'], 'ra': '22017310', 'role': 'DEV', 'stack': 'BACKEND', 'strikes': 0, 'strikes_allowed': 2, 'user_id': '76h35dg4-h76v-1875-987hn-h67gfv45Gt4', 'year': 2}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11991759998', 'course': 'ECM', 'deactivated_date': None, 'email': 'lronald@gmail.com', 'email_dev': 'lronald.devmaua@gmail.com', 'hired_date': 1614567601000, 'hours_worked': 160010000000, 'name': 'Little Ronald', 'photo': None, 'project': ['Maua Food', 'Portfólio', 'Selfie Mauá', 'SMILE'], 'ra': '10017310', 'role': 'DIRECTOR', 'stack': 'FRONTEND', 'strikes': 4, 'strikes_allowed': 4, 'user_id': '6f5g4h7J-876j-0098-123hb-hgb567fy4hb', 'year': 6}},
    {'member': {'active': 'DISCONNECTED', 'cellphone': '11991753208', 'course': 'EMC', 'deactivated_date': None, 'email': 'mneto@gmail.com', 'email_dev': 'mneto.devmaua@gmail.com', 'hired_date': 1614567601000, 'hours_worked': 184430000000, 'name': 'Marcos Pereira Neto', 'photo': None, 'project': ['Selfie Mauá'], 'ra': '19017310', 'role': 'PO', 'stack': 'BUSINESS', 'strikes': 4, 'strikes_allowed': 2, 'user_id': '6574hgyt-785n-9134-18gn4-7gh5uvn36cG', 'year': 4}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11911758098', 'course': 'ECM', 'deactivated_date': None, 'email': 'rubikscube@gmail.com', 'email_dev': 'rcube.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 107350000000, 'name': 'Rubicks Cube', 'photo': None, 'project': ['Selfie Mauá', 'SMILE', 'Gameficação'], 'ra': '19017311', 'role': 'DEV', 'stack': 'BACKEND', 'strikes': 2, 'strikes_allowed': 4, 'user_id': '7gh5yf5H-857H-1234-75hng-94832hvng1s', 'year': 3}},
    {'member': {'active': 'FREEZE', 'cellphone': '11915758098', 'course': 'ECA', 'deactivated_date': None, 'email': 'djangofett@starwars.com', 'email_dev': 'dfett.devmaua@gmail.com', 'hired_date': 1609606565000, 'hours_worked': 79580000000, 'name': 'Django Fett', 'photo': None, 'project': ['SMILE'], 'ra': '17033730', 'role': 'INTERNAL', 'stack': 'INTERNAL', 'strikes': 3, 'strikes_allowed': 2, 'user_id': '7465hvnb-143g-1675-86HnG-75hgnFbcg36', 'year': 2}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11991123498', 'course': 'ECM', 'deactivated_date': None, 'email': 'hsouza@gmail.com', 'email_dev': 'hsouza.devmaua@gmail.com', 'hired_date': 1672592165000, 'hours_worked': 119700000000, 'name': 'Henrique Gustavo de Souza', 'photo': None, 'project': [], 'ra': '22015320', 'role': 'DEV', 'stack': 'UX_UI', 'strikes': 3, 'strikes_allowed': 2, 'user_id': '75648hbr-184n-1985-91han-7ghn4HgF182', 'year': 1}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11991123498', 'course': 'ECM', 'deactivated_date': None, 'email': 'jp@gmail.com', 'email_dev': 'jp.devmaua@gmail.com', 'hired_date': 1672592165000, 'hours_worked': 0, 'name': 'Joao Pedro Soares', 'photo': None, 'project': [], 'ra': '21004102', 'role': 'DEV', 'stack': 'UX_UI', 'strikes': 3, 'strikes_allowed': 2, 'user_id': '9183jBnh-997H-1010-10god-914gHy46tBh', 'year': 1}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11991123498', 'course': 'EPM', 'deactivated_date': None, 'email': 'fernandao@gmail.com', 'email_dev': 'fernandinho.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 0, 'name': 'Fernandao Presidas', 'photo': None, 'project': [], 'ra': '22014322', 'role': 'PO', 'stack': 'BUSINESS', 'strikes': 0, 'strikes_allowed': 2, 'user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', 'year': 3}},
    {'member': {'active': 'ON_HOLD', 'cellphone': '11998472663', 'course': 'ECM', 'deactivated_date': None, 'email': 'carlinhosmiau@gmail.com', 'email_dev': 'carlinhos.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 0, 'name': 'Carlinhos Miau', 'photo': None, 'project': [], 'ra': '23024211', 'role': 'DEV', 'stack': 'BACKEND', 'strikes': 0, 'strikes_allowed': 2, 'user_id': '3b07232f-4f65-42c6-b005-242550b8b8dc', 'year': 3}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11995623456', 'course': 'ECM', 'deactivated_date': None, 'email': 'ryuske@gmail.com', 'email_dev': 'ryuske.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 0, 'name': 'Ryuske', 'photo': None, 'project': [], 'ra': '20123456', 'role': 'DIRECTOR', 'stack': 'RH', 'strikes': 0, 'strikes_allowed': 2, 'user_id': '3b07232f-4f65-42c6-b005-242550b8b8bf', 'year': 5}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11997828564', 'course': 'ADM', 'deactivated_date': None, 'email': 'layala@gmail.com', 'email_dev': 'layala.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 0, 'name': 'Layala Sam', 'photo': None, 'project': [], 'ra': '25123456', 'role': 'INTERNAL', 'stack': 'RH', 'strikes': 0, 'strikes_allowed': 2, 'user_id': '3b07232f-4f65-42c6-b005-242550b8b8ty', 'year': 1}},
    {'member': {'active': 'ACTIVE', 'cellphone': '11997828565', 'course': 'ADM', 'deactivated_date': None, 'email': 'anaju@gmail.com', 'email_dev': 'anaju.devmaua@gmail.com', 'hired_date': 1640192165000, 'hours_worked': 0, 'name': 'Ana Julia', 'photo': None, 'project': [], 'ra': '25123457', 'role': 'INTERNAL', 'stack': 'MKT', 'strikes': 0, 'strikes_allowed': 2, 'user_id': '3b07232f-4f65-42c6-b005-242550b8h9ir', 'year': 1}}
], 'message': 'the members were retrieved'}
        assert response.body['message'] == 'the members were retrieved'
        assert len(response.body['members']) == 14
        assert response.body == expected_dict

    
    def test_get_all_members_controller__requester_user_none(self):
        
        memberrepo = MemberRepositoryMock()
        actionrepo = ActionRepositoryMock()
        strikerepo = StrikeRepositoryMock()
        usecase = GetAllMembersAdminUsecase(memberrepo=memberrepo, actionrepo=actionrepo, strikerepo=strikerepo)
        controller = GetAllMembersAdminController(usecase=usecase)
        request = HttpRequest(body={})
        response = controller(request=request)
        
        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"