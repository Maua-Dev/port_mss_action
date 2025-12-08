from src.modules.get_member.app.get_member_controller import GetMemberController
from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
from pprint import pprint

class Test_GetMemberController:
    member_repo = MemberRepositoryMock()
    action_repo = ActionRepositoryMock()
    strike_repo = StrikeRepositoryMock()
    first_member = member_repo.members[0]
    usecase = GetMemberUsecase(member_repo = member_repo, action_repo = action_repo, strike_repo = strike_repo)
    controller = GetMemberController(usecase)

    def test_get_member_controller(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.first_member.user_id,
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                },
                'start_date': 1624576165000,
                'end_date': 1690046000000
            }
        )

        expected_dict = {'member': {'active': 'ACTIVE',
            'cellphone': '11991758098',
            'course': 'ECA',
            'deactivated_date': None,
            'email': 'vsoller@airubio.com',
            'email_dev': 'vsoller.devmaua@gmail.com',
            'hired_date': 1634576165000,
            'hours_worked': 134460000000,
            'name': 'Vitor Guirão MPNTM',
            'photo': None,
            'project': ['Maua Food', 'Portfólio', 'Selfie Mauá'],
            'ra': '21017310',
            'role': 'DIRECTOR',
            'stack': 'INFRA',
            'strikes': 0,
            'strikes_id': [],
            'strikes_allowed': 4,
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'year': 1},
 'message': 'the member was retrieved'}

        response = self.controller(request)

        pprint(response.body)

        assert response.status_code == 200
        assert response.body == expected_dict

    def test_get_controller_with_invalid_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "Um id no formato inválido",
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_controller_without_id(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": None,
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_controller_with_nonexistentid(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 403
        assert response.body == "That user is not registered"

    def test_get_controller_with_no_request_user(self):
        request = HttpRequest(
            body={

            }
        )

        response = self.controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_get_member_contoller_no_start_date_and_end_date(self):
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": self.first_member.user_id,
                    "name": self.first_member.name,
                    "email": self.first_member.email,
                    "custom:isMaua": True
                }
            }
        )

        expected_dict = {'member': {'active': 'ACTIVE',
            'cellphone': '11991758098',
            'course': 'ECA',
            'deactivated_date': None,
            'email': 'vsoller@airubio.com',
            'email_dev': 'vsoller.devmaua@gmail.com',
            'hired_date': 1634576165000,
            'hours_worked': 0,
            'name': 'Vitor Guirão MPNTM',
            'photo': None,
            'project': ['Maua Food', 'Portfólio', 'Selfie Mauá'],
            'ra': '21017310',
            'role': 'DIRECTOR',
            'stack': 'INFRA',
            'strikes': 0,
            'strikes_id': [],
            'strikes_allowed': 4,
            'user_id': '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
            'year': 1},
 'message': 'the member was retrieved'}

        response = self.controller(request)

        pprint(response.body)

        assert response.status_code == 200
        assert response.body == expected_dict

        #futuramente apos segundo semestre de 2025 teremos que colocar hours_worked : 0