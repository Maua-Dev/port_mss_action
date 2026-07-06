from src.modules.get_member_info.app.get_member_info_controller import GetMemberInfoController
from src.modules.get_member_info.app.get_member_info_usecase import GetMemberInfoUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from pprint import pprint


class Test_GetMemberInfoController:
    member_repo = MemberRepositoryMock()
    action_repo = ActionRepositoryMock()
    first_member = member_repo.members[0]
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

        assert response.status_code == 200
        assert 'homeCarousel' in response.body
        assert 'quoteCarousel' in response.body
        assert 'memberCarousel' in response.body

    def test_get_member_info_controller_with_no_requester_user(self):
        request = HttpRequest(
        )

        response = self.controller(request)

        assert response.status_code == 200
