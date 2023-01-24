import abc
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
from src.shared.domain.entities.action import Action

class AssociatedAction(abc.ABC):
    member_ra: str
    action: Action

    def __init__(self, member_ra: str, action: Action):
        if not AssociatedAction.validate_ra(member_ra):
            raise EntityError("ra")
        self.member_ra = member_ra
        
        if type(action) != Action:
            raise EntityError("action")
        self.action = action

    @staticmethod
    def validate_ra(ra: str) -> bool:
        if ra == None:
            return False
        
        if type(ra) != str:
            raise EntityParameterTypeError("ra must be a string")

        return ra.isdecimal() and len(ra) == 8

    def __repr__(self) -> str:
        return f"AssociatedAction(member_ra={self.member_ra}, action={self.action})"

    def __eq__(self, other) -> bool:
        return self.member_ra == other.member_ra and self.action == other.action