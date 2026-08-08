from src.modules.portfolio_export_members.app.portfolio_export_members_controller import PortfolioExportMembersController
from src.modules.portfolio_export_members.app.portfolio_export_members_usecase import PortfolioExportMembersUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest


class Test_PortfolioExportMembersController:
    member_repo = MemberRepositoryMock()
    action_repo = ActionRepositoryMock()
    first_member = member_repo.members[0]
    usecase = PortfolioExportMembersUsecase(member_repo=member_repo, action_repo=action_repo)
    controller = PortfolioExportMembersController(usecase)

    def test_portfolio_export_members_controller(self):
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

    def test_portfolio_export_members_controller_with_no_requester_user(self):
        request = HttpRequest(
        )

        response = self.controller(request)

        assert response.status_code == 200

    def test_portfolio_export_members_controller_response_structure(self):
        request = HttpRequest(body={})

        response = self.controller(request)

        assert response.status_code == 200
        assert len(response.body['homeCarousel']) == len(self.member_repo.members)
        assert len(response.body['quoteCarousel']) == len(self.member_repo.members)
        assert len(response.body['memberCarousel']) == len(self.member_repo.members)

        assert set(response.body['homeCarousel'][0].keys()) == {'name', 'photoPath', 'area'}
        assert set(response.body['quoteCarousel'][0].keys()) == {'name', 'quote', 'photoPath', 'role'}
        assert set(response.body['memberCarousel'][0].keys()) == {'name', 'photoPath', 'email', 'role', 'phone'}

    def test_portfolio_export_members_controller_with_empty_body(self):
        request = HttpRequest(body={})

        response = self.controller(request)

        assert response.status_code == 200
        assert len(response.body['homeCarousel']) > 0
        assert response.body['homeCarousel'][0]['name'] == self.first_member.name
        assert response.body['homeCarousel'][0]['area'] == self.first_member.stack.value
