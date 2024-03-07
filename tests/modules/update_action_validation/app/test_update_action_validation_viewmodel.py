from src.modules.update_action_validation.app.update_action_validation_view_model import UpdateActionValidationViewModel
from src.shared.domain.entities.action import Action
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock


class TestUpdateActionValidationViewModel:

    def test_update_action_validation_view_model(self):
        repo = ActionRepositoryMock()
        action = repo.actions[0]
        update_action_validation_view_model = UpdateActionValidationViewModel(action)
        
        
        expected = {
            "action": {
                "action_id": "5f4f13df-e7d3-4a10-9219-197ceae9e3f0",
                "is_valid": True
            },
            "message": "Action validation was updated successfully."
        }