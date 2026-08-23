from pprint import pprint

from src.modules.get_hours_chart.app.get_hours_chart_usecase import GetHoursChartUsecase
from src.modules.get_hours_chart.app.get_hours_chart_viewmodel import GetHoursChartViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_GetHoursChartViewmodel:
    def test_get_hours_chart_viewmodel(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = GetHoursChartUsecase(repo=repo, repo_member=repo_member)

        director = repo_member.members[0]
        projects, hours_by_project, hours_by_project_and_stack = usecase(
            user_id=director.user_id, start_date=1637046000000, end_date=1690046000000
        )

        viewmodel = GetHoursChartViewmodel(
            projects=projects, hours_by_project=hours_by_project, hours_by_project_and_stack=hours_by_project_and_stack
        ).to_dict()

        pprint(viewmodel)

        assert viewmodel['message'] == 'the hours chart data was retrieved'

        assert sorted(viewmodel['projects'], key=lambda p: p['code']) == [
            {'code': 'GM', 'name': 'Gameficação'},
            {'code': 'HZ', 'name': 'Zeragem de Horas'},
            {'code': 'MF', 'name': 'Maua Food'},
            {'code': 'PT', 'name': 'Portfólio'},
            {'code': 'SF', 'name': 'Selfie Mauá'},
            {'code': 'SM', 'name': 'SMILE'},
        ]

        assert viewmodel['areas'] == ['BACKEND', 'FRONTEND', 'INFRA', 'UX_UI', 'BUSINESS', 'INTERNAL', 'RH']

        assert viewmodel['hours_by_project'] == {
            'MF': 17255.56, 'PT': 0.0, 'SF': 26813.89, 'SM': 13175.0, 'GM': 366.67, 'HZ': 0.0
        }

        assert viewmodel['hours_by_project_and_area']['MF'] == {
            'BACKEND': 0.0, 'FRONTEND': 0.0, 'INFRA': 5691.67, 'UX_UI': 0.0,
            'BUSINESS': 0.0, 'INTERNAL': 11563.89, 'RH': 0.0
        }
        assert viewmodel['hours_by_project_and_area']['SF'] == {
            'BACKEND': 0.0, 'FRONTEND': 5550.0, 'INFRA': 19088.89, 'UX_UI': 0.0,
            'BUSINESS': 0.0, 'INTERNAL': 2175.0, 'RH': 0.0
        }
        assert viewmodel['hours_by_project_and_area']['GM'] == {
            'BACKEND': 366.67, 'FRONTEND': 0.0, 'INFRA': 0.0, 'UX_UI': 0.0,
            'BUSINESS': 0.0, 'INTERNAL': 0.0, 'RH': 0.0
        }
        assert viewmodel['hours_by_project_and_area']['PT'] == {
            'BACKEND': 0.0, 'FRONTEND': 0.0, 'INFRA': 0.0, 'UX_UI': 0.0,
            'BUSINESS': 0.0, 'INTERNAL': 0.0, 'RH': 0.0
        }

        assert viewmodel['hours_by_area'] == {
            'BACKEND': 366.67, 'FRONTEND': 5550.0, 'INFRA': 31625.0, 'UX_UI': 0.0,
            'BUSINESS': 0.0, 'INTERNAL': 20069.45, 'RH': 0.0
        }

        assert viewmodel['total_hours'] == 57611.12
        assert viewmodel['total_projects'] == 6
        assert viewmodel['active_projects'] == 4

    def test_get_hours_chart_viewmodel_matrix_can_exceed_project_total_when_action_has_multiple_tags(self):
        projects = ActionRepositoryMock().projects
        mf_project = next(p for p in projects if p.code == 'MF')

        hours_by_project = {'MF': 36000000}
        hours_by_project_and_stack = {'MF': {'BACKEND': 36000000, 'FRONTEND': 36000000}}

        viewmodel = GetHoursChartViewmodel(
            projects=[mf_project], hours_by_project=hours_by_project, hours_by_project_and_stack=hours_by_project_and_stack
        ).to_dict()

        assert viewmodel['hours_by_project']['MF'] == 10.0
        assert sum(viewmodel['hours_by_project_and_area']['MF'].values()) == 20.0
        assert viewmodel['total_hours'] == 10.0

    def test_get_hours_chart_viewmodel_empty(self):
        viewmodel = GetHoursChartViewmodel(projects=[], hours_by_project={}, hours_by_project_and_stack={}).to_dict()

        assert viewmodel['projects'] == []
        assert viewmodel['hours_by_project'] == {}
        assert viewmodel['hours_by_project_and_area'] == {}
        assert viewmodel['hours_by_area'] == {
            'BACKEND': 0.0, 'FRONTEND': 0.0, 'INFRA': 0.0, 'UX_UI': 0.0, 'BUSINESS': 0.0, 'INTERNAL': 0.0, 'RH': 0.0
        }
        assert viewmodel['total_hours'] == 0
        assert viewmodel['total_projects'] == 0
        assert viewmodel['active_projects'] == 0