import abc
import uuid
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
from src.shared.domain.entities.action import Action

class AssociatedAction(abc.ABC):
    action_id: str
    start_date: int
    user_id: str

    def __init__(self, action_id: str, start_date: int, user_id: str) -> None:
        
        if not AssociatedAction.validate_action_id(action_id):
            raise EntityError("action_id")
        self.action_id = action_id
        
        if type(start_date) != int:
            raise EntityError("start_date")
        if not 1000000000000 < start_date < 10000000000000:
            raise EntityError("start_date")
        self.start_date = start_date

        if not self.validate_user_id(user_id):
            raise EntityError('user_id')
        self.user_id = user_id

    
    @staticmethod
    def validate_action_id(action_id: str) -> bool:
        if type(action_id) != str:
            return False
        if len(action_id) != Action.ACTION_ID_LENGTH:
            return False
        try:
            uuid.UUID(action_id)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str: return False
        if len(user_id) != Action.USER_ID_LENGTH: return False
        return True

    def __repr__(self) -> str:
        return f"AssociatedAction(user_id={self.user_id}, action={self.action_id})"

    def __eq__(self, other) -> bool:
        return self.user_id == other.user_id and self.action_id == other.action_id