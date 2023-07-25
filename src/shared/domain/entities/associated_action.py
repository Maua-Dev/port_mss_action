import abc
import uuid
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
from src.shared.domain.entities.action import Action

class AssociatedAction(abc.ABC):
    member_ra: str
    action_id: str
    start_date: int

    def __init__(self, member_ra: str, action_id: str, start_date: int):
        if not AssociatedAction.validate_ra(member_ra):
            raise EntityError("ra")
        self.member_ra = member_ra
        
        if not AssociatedAction.validate_action_id(action_id):
            raise EntityError("action_id")
        self.action_id = action_id
        
        if type(start_date) != int:
            raise EntityError("start_date")
        self.start_date = start_date

    @staticmethod
    def validate_ra(ra: str) -> bool:
        if ra == None:
            return False
        
        if type(ra) != str:
            return False

        return ra.isdecimal() and len(ra) == 8
    
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

    def __repr__(self) -> str:
        return f"AssociatedAction(member_ra={self.member_ra}, action={self.action_id})"

    def __eq__(self, other) -> bool:
        return self.member_ra == other.member_ra and self.action_id == other.action_id