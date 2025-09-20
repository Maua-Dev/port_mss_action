from typing import Optional
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY


class StrikeDynamoDTO:
    strike_id: str
    owner_user_id: str
    target_user_id: str
    applier_user_id: str
    occurred_date: int # milisseconds
    category: STRIKE_CATEGORY
    description: Optional [str]

    def __init__(self, strike_id: str, owner_user_id: str, target_user_id: str, applier_user_id: str, occurred_date: int, category: STRIKE_CATEGORY, description: Optional [str]= None):
        self.strike_id= strike_id 

        self.owner_user_id= owner_user_id

        self.target_user_id= target_user_id

        self.applier_user_id= applier_user_id

        self.occurred_date= occurred_date

        self.category= category

        self.description= description

    @staticmethod
    def from_entity(strike: Strike) -> "StrikeDynamoDTO":
        return StrikeDynamoDTO(
            strike_id= strike.strike_id,

            owner_user_id= strike.owner_user_id,

            target_user_id= strike.target_user_id,

            applier_user_id= strike.applier_user_id,

            occurred_date= strike.occurred_date,

            category= strike.category,

            description= strike.description
        )
    
    def to_dynamo(self) -> dict:
        data = {
            "entity": "member",

            "stike_id": self.strike_id,

            "owner_user_id": self.owner_user_id,

            "target_target_user_id": self.target_user_id,

            "applier_user_id": self.applier_user_id,

            "occoured_date": self.occurred_date,

            "category": self.category,

            "description": self.description
        }

        data_without_none_values= {k: v for k, v in data.items() if v is not None}
        return data_without_none_values
    
    @staticmethod
    def from_dynamo(strike_data: dict) -> "StrikeDynamoDTO":
        return StrikeDynamoDTO(
            strike_id= strike_data["strike_id"],

            owner_user_id= strike_data["owner_user_id"],

            target_user_id= strike_data["target_user_id"],

            applier_user_id= strike_data["applier_user_id"],

            occurred_date= int(strike_data["occurred_date"]),

            category=  STRIKE_CATEGORY(strike_data["category"]),

            description= strike_data["description"] if 'description' in strike_data else None
        )
    
    def to_entity(self) -> Strike:
        return Strike(
            strike_id= self.strike_id,

            owner_user_id= self.owner_user_id,

            target_user_id= self.target_user_id,

            applier_user_id= self.applier_user_id,

            occurred_date= self.occurred_date,

            category= self.category,

            description= self.description
        )
    
    def __repr__(self):
        return f"StrikeDynamoDTO(strike_id={self.strike_id}, owner_user_id={self.owner_user_id}, target_user_id={self.target_user_id}, applier_user_id={self.applier_user_id}, occured_date={self.occurred_date}, category={self.category}, description={self.description})"
    
    def __eq__(self, other):
        if not isinstance(other, StrikeDynamoDTO):
            return False
        return self.strike_id == other.strike_id and self.owner_user_id == other.owner_user_id and self.target_user_id == other.target_user_id and self.applier_user_id == other.applier_user_id and self.occurred_date == other.occurred_date and self.category == other.category and self.description == other.description