import pytest

from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.infra.repositories.strike_repository_dynamo import StrikeRepositoryDynamo


class Test_StikeRepositoryDynamo:

    @pytest.mark.skip("Can't run test in github actions")
    def test_create_stike(self):
        repo= StrikeRepositoryDynamo()

        strike= Strike(
            strike_id="a78bea29-9d85-423c-b595-ca5f33d3ea45",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s", applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty", occurred_date=1759574400000, category=STRIKE_CATEGORY.RULE_VIOLATION, description="Teste")

        resp= repo.create_strike(strike=strike)

        assert resp == strike

    @pytest.mark.skip("Can't run test in github actions")
    def test_find_by_id(self):
        repo= StrikeRepositoryDynamo()

        strike= Strike(
            strike_id="a78bea29-9d85-423c-b595-ca5f33d3ea45",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s", applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty", occurred_date=1759574400000, category=STRIKE_CATEGORY.RULE_VIOLATION, description="Teste")

        resp= repo.find_by_id(strike.strike_id)
        assert resp == strike

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_strike_by_target_id(self):
        repo = StrikeRepositoryDynamo()

        strike = Strike(
            strike_id="a78bea29-9d85-423c-b595-ca5f33d3ea45",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s",
            applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty",
            occurred_date=1759574400000,
            category=STRIKE_CATEGORY.RULE_VIOLATION,
            description="Teste"
        )

        resp = repo.get_strike_by_target_id(strike.target_user_id)

        assert resp is not None
        assert isinstance(resp, list)
        assert len(resp) > 0
        assert any(s.strike_id == strike.strike_id for s in resp)

    @pytest.mark.skip("Can't run test in github actions")
    def test_get_all(self):
        repo= StrikeRepositoryDynamo()

        strike= Strike(
            strike_id="a78bea29-9d85-423c-b595-ca5f33d3ea45",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s", applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty", occurred_date=1759574400000, category=STRIKE_CATEGORY.RULE_VIOLATION, description="Teste")

        repo.create_strike(strike=strike)

        resp= repo.get_all()

        assert resp is not None
        assert isinstance(resp, list)
        assert len(resp) > 0
        assert any(s.strike_id == strike.strike_id for s in resp)

        repo.delete_strike(strike_id=strike.strike_id)

    @pytest.mark.skip("Can't run test in github actions")
    def test_delete_strike(self):
        repo= StrikeRepositoryDynamo()

        strike= Strike(
            strike_id="b12bea29-9d85-423c-b595-ca5f33d3ea45",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3", target_user_id="7gh5yf5H-857H-1234-75hng-94832hvng1s", applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8ty", occurred_date=1759574400000, category=STRIKE_CATEGORY.RULE_VIOLATION, description="Teste Delete")

        repo.create_strike(strike=strike)

        resp= repo.delete_strike(strike_id=strike.strike_id)

        assert resp is True