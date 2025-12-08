from src.modules.get_strike.app.get_strike_viewmodel import GetStrikeViewmodel
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from pprint import pprint

class Test_GetStrikeViewModel:
    def test_get_strike_viewmodel(self):
        strike_repo = StrikeRepositoryMock()
        strike = strike_repo.strikes[0]

        viewmodel = GetStrikeViewmodel(strike=strike).to_dict()

        pprint(viewmodel)

        # Montando o esperado manualmente ou baseando-se no objeto
        # Note que a categoria deve virar string no viewmodel
        expected_category = strike.category.value if isinstance(strike.category, STRIKE_CATEGORY) else strike.category

        expected = {
            'strike': {
                'strike_id': strike.strike_id,
                'owner_user_id': strike.owner_user_id,
                'target_user_id': strike.target_user_id,
                'applier_user_id': strike.applier_user_id,
                'occurred_date': strike.occurred_date,
                'category': expected_category,
                'description': strike.description
            },
            'message': 'the strike was retrieved'
        }

        assert viewmodel == expected