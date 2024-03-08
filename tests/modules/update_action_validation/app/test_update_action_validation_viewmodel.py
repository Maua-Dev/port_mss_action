from src.modules.update_action_validation.app.update_action_validation_view_model import UpdateActionValidationViewModel
from src.shared.domain.entities.action import Action
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class TestUpdateActionValidationViewModel:

    def test_update_action_validation_view_model(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        action = repo_action.actions[0]
        member = repo_member.members[0]
        update_action_validation_view_model = UpdateActionValidationViewModel(action).to_dict()
        
        
        expected = {
            "action": {
                "action_id": "5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                "is_valid": True
            },
            "message": "Action validation was updated successfully"
        }

        assert expected == update_action_validation_view_model