from typing import Optional
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY


class CreateStrikeViewmodel:
    strike_id: str
    owner_user_id: str
    target_user_id: str
    applier_user_id: str
    occurred_date: int # milisseconds
    category: STRIKE_CATEGORY
    description: Optional [str]
    case_number: int

    def __init__(self, strike: Strike, case_number: int):
        self.strike_id= strike.strike_id
        self.owner_user_id= strike.owner_user_id
        self.target_user_id= strike.target_user_id
        self.applier_user_id= strike.applier_user_id
        self.occurred_date= strike.occurred_date
        self.category= strike.category
        self.description= strike.description
        self.case_number= case_number

    def to_dict(self):
        model= {
            'strike_id': self.strike_id,
            'owner_user_id': self.owner_user_id,
            'target_user_id': self.target_user_id,
            'applier_user_id': self.applier_user_id,
            'occurred_date': self.occurred_date,
            'category': self.category.value,
            'description': self.description,
            'case_number': self.case_number
        }

        if self.case_number == 0:
            model.update({'message': 'Strike was created successfully'})
            return model

        elif self.case_number == 1:
            model.update({'message': 'Strike was created successfully, hours were reset and an Email was sent to Directors and Heads'})
            return model