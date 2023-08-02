from src.modules.get_history.app.get_history_usecase import GetHistoryUsecase
from src.modules.get_history.app.get_history_viewmodel import GetHistoryViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetHistoryViewmodel:
    def test_get_history_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        actions, last_evaluated_key = usecase(ra='17033730')
        viewmodel = GetHistoryViewmodel(
            actions=actions, last_evaluated_key=last_evaluated_key).to_dict()

        expected = {
            'actions': [
                {
                    'owner_ra': '19017310',
                    'start_date': 1688646000000,
                    'end_date': 1689966000000,
                    'duration': 1320000000,
                    'action_id': '46b35022-1a68-4cc8-a2e5-ae449e43e867',
                    'story_id': 237,
                    'title': 'Revisão',
                    'description': 'Sprint Planning',
                    'project_code': 'GM',
                    'associated_members_ra': [
                        '10017310',
                        '23017310',
                        '19017311',
                        '17033730',
                        '22017310'
                    ],
                    'stack_tags':[
                        'BACKEND'
                    ],
                    'action_type_tag':'WORK'
                },
                {
                    'owner_ra': '19017310',
                    'start_date': 1667256000000,
                    'end_date': 1690046000000,
                    'duration': 22790000000,
                    'action_id': 'eefe6db8-e03e-42c3-9fd2-1de796139501',
                    'story_id': 497,
                    'title': 'Retrospective',
                    'description': 'Reunião de planning',
                    'project_code': 'SM',
                    'associated_members_ra': [
                        '23017310',
                        '10017310',
                        '17033730'
                    ],
                    'stack_tags':[
                        'INTERNAL'
                    ],
                    'action_type_tag':'ARCHITECT'
                },
                {
                    'owner_ra': '10017310',
                    'start_date': 1663116000000,
                    'end_date': 1683606000000,
                    'duration': 20490000000,
                    'action_id': '87d4a661-0752-4ce2-9440-05e752e636fc',
                    'story_id': 932,
                    'title': 'Desenvolvimento',
                    'description': 'Revisão de sprint',
                    'project_code': 'MF',
                    'associated_members_ra': [
                        '21010757',
                        '17033730',
                        '19017310',
                        '23017310'
                    ],
                    'stack_tags':[
                        'INFRA'
                    ],
                    'action_type_tag':'LEARN'
                },
                {
                    'owner_ra': '19017311',
                    'start_date': 1658136000000,
                    'end_date': 1678116000000,
                    'duration': 19980000000,
                    'action_id': 'ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                    'story_id': 435,
                    'title': 'Retrospective',
                    'description': 'Reunião de planning',
                    'project_code': 'SF',
                    'associated_members_ra': [
                        '17033730',
                        '22017310',
                        '10017310',
                        '23017310',
                        '21017310'
                    ],
                    'stack_tags':[
                        'FRONTEND'
                    ],
                    'action_type_tag':'DESIGN'
                },
                {
                    'owner_ra': '10017310',
                    'start_date': 1641896000000,
                    'end_date': 1679686000000,
                    'duration': 37790000000,
                    'action_id': '42e01f11-283c-4925-b0aa-e80ac6c1815a',
                    'story_id': 983,
                    'title': 'Retrospectiva',
                    'description': 'Revisão de sprint',
                    'project_code': 'SF',
                    'associated_members_ra': [
                        '21017310',
                        '19017310',
                        '19017311',
                        '23017310',
                        '17033730'
                    ],
                    'stack_tags':[
                        'INFRA'
                    ],
                    'action_type_tag':'WORK'
                }
            ],
            'last_evaluated_key': '42e01f11-283c-4925-b0aa-e80ac6c1815a',
            'message': 'the history was retrieved'
        }

        assert viewmodel == expected