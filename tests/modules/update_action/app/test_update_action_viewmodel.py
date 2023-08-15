from src.modules.update_action.app.update_action_usecase import UpdateActionUsecase
from src.modules.update_action.app.update_action_viewmodel import UpdateActionViewmodel
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class Test_UpdateActionViewmodel:
    def test_update_action_viewmodel(self):
        repo = ActionRepositoryMock()
        usecase = UpdateActionUsecase(repo)
        action = usecase(
            action_id=repo.actions[0].action_id, new_owner_ra='22011020')

        viewmodel = UpdateActionViewmodel(action=action).to_dict()
        expected = {
            'action': {
                'owner_ra': '22011020',
                'start_date': 1644256000000,
                'end_date': 1653756000000,
                'duration': 9500000000,
                'action_id': '5f4f13df-e7d3-4a10-9219-197ceae9e3f0',
                'story_id': 94,
                'title': 'Retrospectiva',
                'description': 'Revisão de sprint',
                'project_code': 'PT',
                'associated_members_ra': [
                    '23017310',
                    '21010757',
                    '22017310',
                    '21017310',
                    '19017310',
                    '19017311'
                ],
                'stack_tags': [
                    'INFRA'
                ],
                'action_type_tag': 'CODEREVIEW'
            },
            'message': 'the action was updated'
        }
        
        assert viewmodel == expected