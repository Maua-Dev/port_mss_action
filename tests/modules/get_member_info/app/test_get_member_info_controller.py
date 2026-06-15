from src.modules.get_member_info.app.get_member_info_controller import GetMemberInfoController
from src.modules.get_member_info.app.get_member_info_usecase import GetMemberInfoUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from pprint import pprint


class Test_GetMemberInfoController:
    member_repo = MemberRepositoryMock()
    action_repo = ActionRepositoryMock()
    first_member = member_repo.members[0]  # Vitor Guirão
    usecase = GetMemberInfoUsecase(member_repo=member_repo, action_repo=action_repo)
    controller = GetMemberInfoController(usecase)

    def test_get_member_info_controller(self):
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

        response = self.controller(request)

        pprint(response.body)

        assert response.status_code == 200
        assert 'ALL' in response.body
        assert type(response.body['ALL']) == list
        assert len(response.body['ALL']) > 0

    def test_get_member_info_controller_with_invalid_id(self):
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

    def test_get_member_info_controller_without_id(self):
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

    def test_get_member_info_controller_with_nonexistent_id(self):
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

    def test_get_member_info_controller_with_no_requester_user(self):
        request = HttpRequest(
            body={}
        )

        response = self.controller(request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"

    def test_get_member_info_controller_freeze_user(self):
        # Luigi Televisão - FREEZE
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "76h35dg4-h76v-1875-987hn-h67gfv45Gt4",
                    "name": "Luigi Televisão",
                    "email": "lgtv@gmail.com",
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 403

    def test_get_member_info_controller_disconnected_user(self):
        # Marcos Pereira Neto - DISCONNECTED
        request = HttpRequest(
            body={
                'requester_user': {
                    "sub": "6574hgyt-785n-9134-18gn4-7gh5uvn36cG",
                    "name": "Marcos Pereira Neto",
                    "email": "mneto@gmail.com",
                    "custom:isMaua": True
                }
            }
        )

        response = self.controller(request)

        assert response.status_code == 403