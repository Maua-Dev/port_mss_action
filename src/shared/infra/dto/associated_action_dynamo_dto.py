from decimal import Decimal

from src.shared.domain.entities.associated_action import AssociatedAction


class AssociatedActionDynamoDTO:
    action_id: str
    start_date: int
    user_id: str
    
    def __init__(self, action_id: str, start_date: int, user_id: str):
        self.action_id = action_id
        self.start_date = start_date
        self.user_id = user_id
        
    @staticmethod
    def from_entity(self) -> "AssociatedActionDynamoDTO":
        return AssociatedActionDynamoDTO(
            action_id=self.action_id,
            start_date=self.start_date,
            user_id=self.user_id
        )
        
    def to_dynamo(self) -> dict:
        return {
            "entity": "associated_action",
            "action_id": self.action_id,
            "start_date": Decimal(str(self.start_date)),
            "user_id": self.user_id
        }
        
    @staticmethod
    def from_dynamo(data: dict) -> "AssociatedActionDynamoDTO":
        return AssociatedActionDynamoDTO(
            action_id=data['action_id'],
            start_date=int(data['start_date']),
            user_id=data['user_id']
        )
        
    def to_entity(self) -> AssociatedAction:
        return AssociatedAction(
            action_id=self.action_id,
            start_date=self.start_date,
            user_id=self.user_id
        )
        
    def __repr__(self):
        return f"AssociatedActionDynamoDTO(action_id={self.action_id}, start_date={self.start_date}, user_id={self.user_id})"
    
    def __eq__(self, other):
        if not isinstance(other, AssociatedActionDynamoDTO):
            return False
        return self.action_id == other.action_id and self.start_date == other.start_date and self.user_id == other.user_id