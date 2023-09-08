from decimal import Decimal

from src.shared.domain.entities.associated_action import AssociatedAction


class AssociatedActionDynamoDTO:
    member_ra: str
    action_id: str
    start_date: int
    
    def __init__(self, member_ra: str, action_id: str, start_date: int):
        self.member_ra = member_ra
        self.action_id = action_id
        self.start_date = start_date
        
    @staticmethod
    def from_entity(self) -> "AssociatedActionDynamoDTO":
        return AssociatedActionDynamoDTO(
            member_ra=self.member_ra,
            action_id=self.action_id,
            start_date=self.start_date
        )
        
    def to_dynamo(self) -> dict:
        return {
            "entity": "associated_action",
            "member_ra": self.member_ra,
            "action_id": self.action_id,
            "start_date": Decimal(str(self.start_date))
        }
        
    @staticmethod
    def from_dynamo(data: dict) -> "AssociatedActionDynamoDTO":
        return AssociatedActionDynamoDTO(
            member_ra=data['member_ra'],
            action_id=data['action_id'],
            start_date=int(data['start_date'])
        )
        
    def to_entity(self) -> AssociatedAction:
        return AssociatedAction(
            member_ra=self.member_ra,
            action_id=self.action_id,
            start_date=self.start_date
        )
        
    def __repr__(self):
        return f"AssociatedActionDynamoDTO(member_ra={self.member_ra}, action_id={self.action_id}, start_date={self.start_date}"
    
    def __eq__(self, other):
        if not isinstance(other, AssociatedActionDynamoDTO):
            return False
        return self.member_ra == other.member_ra and self.action_id == other.action_id and self.start_date == other.start_date