from src.modules.get_hours_chart.app.get_hours_chart_controller import GetHoursChartController
from src.modules.get_hours_chart.app.get_hours_chart_usecase import GetHoursChartUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetHoursChartController:
    def test_get_hours_chart_controller(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        director = repo_member.members[0]
        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": director.user_id,
                    "name": director.name,
                    "email": director.email,
                    "custom:isMaua": True
                },
            },
            query_params={"start_date": 1637046000000, "end_date": 1690046000000}
        )
        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['message'] == 'the hours chart data was retrieved'
        assert len(response.body['projects']) == len(repo.projects)
        assert response.body['areas'] == ['BACKEND', 'FRONTEND', 'INFRA', 'UX_UI', 'BUSINESS', 'INTERNAL', 'RH']
        assert response.body['hours_by_project']['MF'] == 17255.56

    def test_get_hours_chart_controller_no_dates(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        director = repo_member.members[0]
        request = HttpRequest(body={
            "requester_user": {
                "sub": director.user_id,
                "name": director.name,
                "email": director.email,
                "custom:isMaua": True
            },
        })
        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['message'] == 'the hours chart data was retrieved'

    def test_get_hours_chart_controller_missing_requester_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        request = HttpRequest(body={})
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    def test_get_hours_chart_controller_forbidden_regular_dev(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        dev = next(m for m in repo_member.members if m.user_id == "7gh5yf5H-857H-1234-75hng-94832hvng1s")
        request = HttpRequest(body={
            "requester_user": {
                "sub": dev.user_id,
                "name": dev.name,
                "email": dev.email,
                "custom:isMaua": True
            },
        })
        response = controller(request=request)

        assert response.status_code == 403

    def test_get_hours_chart_controller_user_not_found(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        request = HttpRequest(body={
            "requester_user": {
                "sub": "00000000-0000-0000-0000-000000000000",
                "name": "Fulano",
                "email": "fulano@maua.br",
                "custom:isMaua": True
            },
        })
        response = controller(request=request)

        assert response.status_code == 404

    def test_get_hours_chart_controller_start_date_as_numeric_string_from_real_querystring(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        director = repo_member.members[0]
        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": director.user_id,
                    "name": director.name,
                    "email": director.email,
                    "custom:isMaua": True
                },
            },
            query_params={"start_date": "1637046000000", "end_date": "1690046000000"}
        )
        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['hours_by_project']['MF'] == 17255.56

    def test_get_hours_chart_controller_wrong_type_start_date(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        director = repo_member.members[0]
        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": director.user_id,
                    "name": director.name,
                    "email": director.email,
                    "custom:isMaua": True
                },
            },
            query_params={"start_date": "nao-e-uma-data"}
        )
        response = controller(request=request)

        assert response.status_code == 400

    def test_get_hours_chart_controller_start_date_after_end_date(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)
        controller = GetHoursChartController(usecase=usecase)

        director = repo_member.members[0]
        request = HttpRequest(
            body={
                "requester_user": {
                    "sub": director.user_id,
                    "name": director.name,
                    "email": director.email,
                    "custom:isMaua": True
                },
            },
            query_params={"start_date": 1690046000000, "end_date": 1637046000000}
        )
        response = controller(request=request)

        assert response.status_code == 400