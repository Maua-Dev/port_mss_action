from src.modules.update_action_validation.app.update_action_validation_viewmodel import UpdateActionValidationViewModel
from src.shared.domain.entities.action import Action
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class TestUpdateActionValidationViewModel:

    def test_update_action_validation_view_model(self):
        repo_action = ActionRepositoryMock()
        repo_member = MemberRepositoryMock()
        action = repo_action.actions[0]
        user_id = repo_member.members[0].user_id
        update_action_validation_view_model = UpdateActionValidationViewModel(action.action_id, action.is_valid, user_id).to_dict()
        
        
        expected = {
            "action": {
                "action_id": "5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                "is_valid": True,
                "user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
            },
            "message": "Action validation was updated successfully"
        }

        assert expected == update_action_validation_view_model