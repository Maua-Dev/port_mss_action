from src.shared.domain.entities.action import Action

class ActionValidationViewModel:
    action_id: str
    is_valid: bool
    
    def __init__(self, action: Action):
        self.action_id = action.action_id
        self.is_valid = action.is_valid
    
    def to_dict(self) -> dict:
        return {
            'action_id' : self.action_id,
            'is_valid' : self.is_valid
        }
    
class UpdateActionValidationViewModel:
    action: ActionValidationViewModel
    
    def __init__(self, action: Action):
        self.action = ActionValidationViewModel(action)

    def to_dict(self) -> dict:
        return {
            "action": self.action.to_dict(),
            "message": "Action validation was updated successfully."
        }