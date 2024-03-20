from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.modules.update_action.app.update_action_viewmodel import UpdateActionViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_UpdateActionViewmodel:
    def test_update_action_viewmodel(self):
        repo = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        usecase = UpdateActionUsecase(repo, repo_member=repo_member)
        action = usecase(
            action_id=repo.actions[0].action_id, new_user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3')

        viewmodel = UpdateActionViewmodel(action=action).to_dict()
        expected = {
            'action': {
                'user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
                'start_date': 1644256000000,
                'end_date': 1653756000000,
                'is_valid': True,
                'duration': 9500000000,
                'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                'story_id': 94,
                'title': 'Retrospectiva',
                'description': 'Revisão de sprint',
                'project_code': 'PT',
                'associated_members_user_ids': ["75648hbr-184n-1985-91han-7ghn4HgF182", "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "76h35dg4-h76v-1875-987hn-h67gfv45Gt4", "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "6574hgyt-785n-9134-18gn4-7gh5uvn36cG", "7gh5yf5H-857H-1234-75hng-94832hvng1s"],
                'stack_tags': [
                    'INFRA'
                ],
                'action_type_tag': 'CODEREVIEW'
            },
            'message': 'the action was updated'
        }
        print(viewmodel)
        assert viewmodel == expected