from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.infra.dto.strike_dynamo_dto import StrikeDynamoDTO

class Test_StrikeDynamoDTO:

    def test_strike_dynamo_dto_from_entity(self):
        strike = Strike(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

        strike_dto = StrikeDynamoDTO.from_entity(strike)

        assert strike_dto == StrikeDynamoDTO(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

    def test_strike_dynamo_dto_to_dynamo(self):
        strike_dto = StrikeDynamoDTO(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

        strike_dynamo = strike_dto.to_dynamo()

        assert strike_dynamo == {
            "entity": "strike",
            "strike_id": "46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            "target_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            "applier_user_id": "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            "occurred_date": 1577847600000,
            "category": "MISCONDUCT",
            "description": "Teste de strike."
        }

    def test_strike_dynamo_dto_from_dynamo(self):
        strike_dynamo = {
            "entity": "strike",
            "strike_id": "46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            "target_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            "applier_user_id": "6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            "occurred_date": 1577847600000,
            "category": "MISCONDUCT",
            "description": "Teste de strike."
        }

        strike_dto = StrikeDynamoDTO.from_dynamo(strike_dynamo)

        assert strike_dto == StrikeDynamoDTO(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

    def test_strike_dynamo_dto_to_entity(self):
        strike_dto = StrikeDynamoDTO(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

        strike = strike_dto.to_entity()

        assert strike == Strike(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Teste de strike."
        )

    def test_strike_dynamo_dto_optional_description(self):
        strike = Strike(
            strike_id="46b7ed28-02d9-4ea3-9f8b-85cd8708d846",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="51ah5jaj-c9jm-1345-666ab-e12341c14a3",
            applier_user_id="6f5g4h7J-876j-0098-123hb-hgb567fy4hb",
            occurred_date=1577847600000,
            category=STRIKE_CATEGORY.RULE_VIOLATION
        )

        strike_dto = StrikeDynamoDTO.from_entity(strike)
        strike_dynamo = strike_dto.to_dynamo()
        strike_entity = strike_dto.to_entity()

        assert strike_dto.description is None
        assert "description" not in strike_dynamo
        assert strike_entity.description is None
