from src.shared.domain.entities.action import Action

class ActionValidationViewModel:
    action_id: str
    is_valid: bool
    user_id: str
    
    def __init__(self, action: Action, user_id: str):
        self.action_id = action.action_id
        self.is_valid = action.is_valid
        self.user_id = user_id
    
    def to_dict(self) -> dict:
        return {
            'action_id' : self.action_id,
            'is_valid' : self.is_valid,
            'user_id' : self.user_id
        }
    
class UpdateActionValidationViewModel:
    action: ActionValidationViewModel
    
    def __init__(self, action: Action, user_id: str):
        self.action = ActionValidationViewModel(action, user_id)

    def to_dict(self) -> dict:
        return {
            "action": self.action.to_dict(),
            "message": "Action validation was updated successfully"
        }