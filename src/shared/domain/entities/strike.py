from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
import abc
from typing import Optional
from enum import Enum
from src.shared.helpers.errors.domain_errors import EntityError

class Strike(abc.ABC):
    strike_id: str
    owner_user_id: str
    target_user_id: str
    applier_user_id: str
    ocurred_date: int # milisseconds
    category: STRIKE_CATEGORY
    description: Optional [str]
    MAX_DESCRIPTION_LENGTH = 500
    STRIKE_ID_LENGTH = 36
    OWNER_USER_ID_LENGTH = 36
    TARGET_USER_ID_LENGTH = 36
    APPLIER_USER_ID_LENGTH = 36

    def __init__(self, strike_id: str, owner_user_id: str, target_user_id: str, applier_user_id: str, ocurred_date: int, category: STRIKE_CATEGORY, description: Optional[str] = None):

        if not self.validate_strike_id(strike_id):
            raise EntityError('strike_id')
        self.strike_id = strike_id

        if not self.validate_owner_user_id(owner_user_id):
            raise EntityError('owner_user_id')
        self.owner_user_id = owner_user_id

        if not self.validate_target_user_id(target_user_id):
            raise EntityError('target_user_id')
        self.target_user_id = target_user_id

        if not self.validate_applier_user_id(applier_user_id):
            raise EntityError('applier_user_id')
        self.applier_user_id = applier_user_id

        if not self.validate_description(description):
            raise EntityError('description')
        self.description = description

        if type(ocurred_date) != int:
            raise EntityError('ocurred_date')
        self.ocurred_date = ocurred_date
        if type(category) != STRIKE_CATEGORY:
            raise EntityError('category')
        self.category = category

    @staticmethod
    def validate_strike_id(strike_id: str) -> bool:
        if type(strike_id) != str:
            return False
        if len(strike_id) != Strike.STRIKE_ID_LENGTH:
            return False
        return True

    @staticmethod
    def validate_owner_user_id(owner_user_id: str) -> bool:
        if type(owner_user_id) != str:
            return False
        if len(owner_user_id) != Strike.OWNER_USER_ID_LENGTH:
            return False
        return True

    @staticmethod
    def validate_target_user_id(target_user_id: str) -> bool:
        if type(target_user_id) != str:
            return False
        if len(target_user_id) != Strike.TARGET_USER_ID_LENGTH:
            return False
        return True

    @staticmethod
    def validate_applier_user_id(applier_user_id: str) -> bool:
        if type(applier_user_id) != str:
            return False
        if len(applier_user_id) != Strike.APPLIER_USER_ID_LENGTH:
            return False
        return True

    @staticmethod
    def validate_description(description: Optional[str]) -> bool:
        if description is not None:
          if type(description) != str:
              return False
          if len(description) > Strike.MAX_DESCRIPTION_LENGTH:
              return False
        return True

    def __repr__(self):
        return f"<Strike> (strike_id: {self.strike_id}, owner_user_id: {self.owner_user_id}, target_user_id: {self.target_user_id}, applier_user_id: {self.applier_user_id}, ocurred_date: {self.ocurred_date}, category: {self.category}, description: {self.description})"

    def __eq__(self, other):
        if not isinstance(other, Strike):
            return False

        return self.strike_id == other.strike_id and self.owner_user_id == other.owner_user_id and self.target_user_id == other.target_user_id and self.applier_user_id == other.applier_user_id and self.ocurred_date == other.ocurred_date and self.category == other.category and self.description == other.description