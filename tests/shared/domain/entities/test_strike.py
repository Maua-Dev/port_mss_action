import pytest
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
import abc
from typing import Optional
from enum import Enum
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Strike:
    def test_strike(self):
        strike = Strike(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

        assert strike.strike_id == "46b7ed28-02d9-4ea3-9f8b-85cd8708d846"
        assert strike.owner_user_id == "93bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert strike.target_user_id == "51ah5jaj-c9jm-1345-666ab-e12341c14a3"
        assert strike.applier_user_id == "6f5g4h7J-876j-0098-123hb-hgb567fy4hb"
        assert strike.occurred_date == 1577847600000
        assert strike.category == STRIKE_CATEGORY.MISCONDUCT
        assert strike.description == "Teste de strike."

    def test_strike_id_not_str(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id=123,
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_strike_id_invalid_length(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="123",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_owner_user_id_not_str(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id=123,
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_owner_user_id_invalid_length(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="123",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_target_user_id_not_str(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id=123,
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_target_user_id_invalid_length(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="123",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_applier_user_id_not_str(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id=123,
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_applier_user_id_invalid_length(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="123",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_description_not_str(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description=123
            )

    def test_description_too_long(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="x" * 501
            )

    def test_occurred_date_not_int(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date="1577847600000",
                category=STRIKE_CATEGORY.MISCONDUCT,
                description="Teste de strike."
            )

    def test_category_not_enum(self):
        with pytest.raises(EntityError):
            Strike(
                strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
                owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
                occurred_date=1577847600000,
                category="MISCONDUCT",
                description="Teste de strike."
            )