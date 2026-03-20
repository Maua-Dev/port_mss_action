from typing import Optional
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY


class StrikeViewModel:
    strike_id: str
    owner_user_id: str
    target_user_id: str
    applier_user_id: str
    occurred_date: int
    category: STRIKE_CATEGORY
    description: Optional [str]

    def __init__(self, strike: Strike):
        self.strike_id = strike.strike_id
        self.owner_user_id = strike.owner_user_id
        self.target_user_id = strike.target_user_id
        self.applier_user_id = strike.applier_user_id
        self.occurred_date = strike.occurred_date
        self.category = strike.category
        self.description = strike.description

    def to_dict(self):
        return {
            'strike_id': self.strike_id,
            'owner_user_id': self.owner_user_id,
            'target_user_id': self.target_user_id,
            'applier_user_id': self.applier_user_id,
            'occurred_date': self.occurred_date,
            'category': self.category.value,
            'description': self.description
        }

class DeleteStrikeViewModel:
    strike: Strike

    def __init__(self, strike: Strike):
        self.strike = strike

    def to_dict(self) -> dict:
        strike_dict = StrikeViewModel(self.strike).to_dict()
        strike_dict['is_valid'] = True
        return {
            'strike': strike_dict,
            'message' : 'the strike was deleted successfully'
        }