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