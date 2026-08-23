import pytest

from src.modules.get_hours_chart.app.get_hours_chart_usecase import GetHoursChartUsecase
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.helpers.errors.usecase_errors import UnregisteredUser, UserIsNotFromAdmin, UserNotAllowed
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetHoursChartUsecase:
    def test_get_hours_chart_usecase_director(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        director = repo_member.members[0]
        assert director.role.value == "DIRECTOR"

        projects, hours_by_project, hours_by_project_and_stack = usecase(
            user_id=director.user_id, start_date=1637046000000, end_date=1690046000000
        )

        assert type(projects) == list
        assert all([type(p) == Project for p in projects])
        assert len(projects) == 6

        assert hours_by_project == {'GM': 1320000000, 'MF': 62120000000, 'SF': 96530000000, 'SM': 47430000000}
        assert hours_by_project_and_stack == {
            'GM': {'BACKEND': 1320000000},
            'MF': {'INFRA': 20490000000, 'INTERNAL': 41630000000},
            'SF': {'FRONTEND': 19980000000, 'INFRA': 68720000000, 'INTERNAL': 7830000000},
            'SM': {'INFRA': 24640000000, 'INTERNAL': 22790000000},
        }

    def test_get_hours_chart_usecase_head(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        head = repo_member.members[1]
        assert head.role.value == "HEAD"

        projects, hours_by_project, hours_by_project_and_stack = usecase(user_id=head.user_id)
        assert type(projects) == list

    def test_get_hours_chart_usecase_business_stack_non_admin_role(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        business_member = next(m for m in repo_member.members if m.user_id == "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0")
        assert business_member.stack.value == "BUSINESS"
        assert business_member.role.value != "DIRECTOR"
        assert business_member.role.value != "HEAD"

        projects, hours_by_project, hours_by_project_and_stack = usecase(
            user_id=business_member.user_id, start_date=1637046000000, end_date=1690046000000
        )
        assert type(projects) == list
        assert len(projects) == 6

    def test_get_hours_chart_usecase_rh_stack_non_admin_role(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        rh_member = next(m for m in repo_member.members if m.user_id == "3b07232f-4f65-42c6-b005-242550b8b8ty")
        assert rh_member.stack.value == "RH"
        assert rh_member.role.value != "DIRECTOR"
        assert rh_member.role.value != "HEAD"

        projects, hours_by_project, hours_by_project_and_stack = usecase(
            user_id=rh_member.user_id, start_date=1637046000000, end_date=1690046000000
        )
        assert type(projects) == list

    def test_get_hours_chart_usecase_forbidden_regular_dev(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        dev = next(m for m in repo_member.members if m.user_id == "7gh5yf5H-857H-1234-75hng-94832hvng1s")
        assert dev.role.value == "DEV"
        assert dev.stack.value == "BACKEND"

        with pytest.raises(UserIsNotFromAdmin):
            usecase(user_id=dev.user_id)

    def test_get_hours_chart_usecase_not_found_user_id(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        with pytest.raises(UnregisteredUser):
            usecase(user_id="user-que-nao-existe")

    def test_get_hours_chart_usecase_inactive_user(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        freeze_user = next(m for m in repo_member.members if m.active == ACTIVE.FREEZE)

        with pytest.raises(UserNotAllowed):
            usecase(user_id=freeze_user.user_id)

    def test_get_hours_chart_usecase_no_start_and_end_date(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        director = repo_member.members[0]
        projects, hours_by_project, hours_by_project_and_stack = usecase(user_id=director.user_id)

        assert type(projects) == list
        assert len(projects) == 6
        assert type(hours_by_project) == dict
        assert type(hours_by_project_and_stack) == dict