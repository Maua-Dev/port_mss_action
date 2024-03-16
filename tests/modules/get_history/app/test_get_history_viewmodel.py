from src.modules.get_history.app.get_history_usecase import GetHistoryUsecase
from src.modules.get_history.app.get_history_viewmodel import GetHistoryViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_GetHistoryViewmodel:
    def test_get_history_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        actions, last_evaluated_key = usecase(user_id='7465hvnb-143g-1675-86HnG-75hgnFbcg36')
        viewmodel = GetHistoryViewmodel(
            actions=actions, last_evaluated_key=last_evaluated_key).to_dict()

        expected = {
            'actions': [
                {
                    'start_date': 1688646000000,
                    'end_date': 1689966000000,
                    'duration': 1320000000,
                    'action_id': '46b35022-1a68-4cc8-a2e5-ae449e43e867',
                    'story_id': 237,
                    'title': 'Revisão',
                    'description': 'Sprint Planning',
                    'project_code': 'GM',
                    'associated_members_user_ids': [
                        '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                        '75648hbr-184n-1985-91han-7ghn4HgF182',
                        '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                        '7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                        '76h35dg4-h76v-1875-987hn-h67gfv45Gt4'
                    ],
                    'stack_tags': ['BACKEND'],
                    'action_type_tag': 'WORK'
                },
                {
                    'start_date': 1667256000000,
                    'end_date': 1690046000000,
                    'duration': 22790000000,
                    'action_id': 'eefe6db8-e03e-42c3-9fd2-1de796139501',
                    'story_id': 497,
                    'title': 'Retrospective',
                    'description': 'Reunião de planning',
                    'project_code': 'SM',
                    'associated_members_user_ids': [
                        '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                        '75648hbr-184n-1985-91han-7ghn4HgF182',
                        '6f5g4h7J-876j-0098-123hb-hgb567fy4hb'
                    ],
                    'stack_tags': ['INTERNAL'],
                    'action_type_tag': 'ARCHITECT'
                },
                {
                    'start_date': 1663116000000,
                    'end_date': 1683606000000,
                    'duration': 20490000000,
                    'action_id': '87d4a661-0752-4ce2-9440-05e752e636fc',
                    'story_id': 932,
                    'title': 'Desenvolvimento',
                    'description': 'Revisão de sprint',
                    'project_code': 'MF',
                    'associated_members_user_ids': [
                        '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                        '75648hbr-184n-1985-91han-7ghn4HgF182',
                        '7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                        '51ah5jaj-c9jm-1345-666ab-e12341c14a3'
                    ],
                    'stack_tags': ['INFRA'],
                    'action_type_tag': 'LEARN'
                },
                {
                    'start_date': 1658136000000,
                    'end_date': 1678116000000,
                    'duration': 19980000000,
                    'action_id': 'ea95d4f7-d5ce-4944-9fa1-ab964655294b',
                    'story_id': 435,
                    'title': 'Retrospective',
                    'description': 'Reunião de planning',
                    'project_code': 'SF',
                    'associated_members_user_ids': [
                        '7465hvnb-143g-1675-86HnG-75hgnFbcg36',
                        '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                        '76h35dg4-h76v-1875-987hn-h67gfv45Gt4',
                        '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
                        '75648hbr-184n-1985-91han-7ghn4HgF182'
                    ],
                    'stack_tags': ['FRONTEND'],
                    'action_type_tag': 'DESIGN'
                },
                {
                    'start_date': 1641896000000,
                    'end_date': 1679686000000,
                    'duration': 37790000000,
                    'action_id': '42e01f11-283c-4925-b0aa-e80ac6c1815a',
                    'story_id': 983,
                    'title': 'Retrospectiva',
                    'description': 'Revisão de sprint',
                    'project_code': 'SF',
                    'associated_members_user_ids': [
                        '6574hgyt-785n-9134-18gn4-7gh5uvn36cG',
                        '7gh5yf5H-857H-1234-75hng-94832hvng1s',
                        '75648hbr-184n-1985-91han-7ghn4HgF182',
                        '93bc6ada-c0d1-7054-66ab-e17414c48ae3',
                        '7465hvnb-143g-1675-86HnG-75hgnFbcg36'
                    ],
                    'stack_tags': ['INFRA'],
                    'action_type_tag': 'WORK'
                }
            ],
            'last_evaluated_key': {
                'action_id': '42e01f11-283c-4925-b0aa-e80ac6c1815a',
                'start_date': 1641896000000
            },
            'message': 'the history was retrieved'
        }

        assert viewmodel == expected
        
    def test_get_history_viewmodel_with_no_actions(self):
        repo = ActionRepositoryMock()
        usecase = GetHistoryUsecase(repo)
        actions, last_evaluated_key = usecase(user_id='6fag4h7J-876j-0098-123hb-hgb567fy4hb')
        viewmodel = GetHistoryViewmodel(
            actions=actions, last_evaluated_key=last_evaluated_key).to_dict()

        expected = {
            'actions': [],
            'last_evaluated_key': None,
            'message': 'the history was retrieved'
        }

        assert viewmodel == expected