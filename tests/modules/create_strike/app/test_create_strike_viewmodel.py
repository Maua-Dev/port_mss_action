from src.modules.create_strike.app.create_strike_viewmodel import CreateStrikeViewmodel
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_CreateStrikeViewmodel:
    def test_create_strike_viewmodel_case_0(self):

        strike= Strike(
            strike_id='n4o5p6q7-r8s9-0123-4567-890123nopqtu',
            owner_user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            target_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', 
            applier_user_id='3b07232f-4f65-42c6-b005-242550b8b8bf',
            occurred_date=1725512986000, 
            category=STRIKE_CATEGORY.OTHER,
            description='testing creating a strike',
        )
        
        new_strike= CreateStrikeViewmodel(strike=strike, case_number=0)

        expected = {
            'strike_id': 'n4o5p6q7-r8s9-0123-4567-890123nopqtu',
            'owner_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            'target_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', 
            'applier_user_id': '3b07232f-4f65-42c6-b005-242550b8b8bf',
            'occurred_date': 1725512986000, 
            'category': STRIKE_CATEGORY.OTHER,
            'description': 'testing creating a strike',
            'case_number': 0,
            'message': 'Strike was created successfully'
        }

        assert new_strike.to_dict() == expected


    def test_create_strike_viewmodel_case_1(self):

        strike= Strike(
            strike_id='n4o5p6q7-r8s9-0123-4567-890123nopqtu',
            owner_user_id='51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            target_user_id='5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', 
            applier_user_id='3b07232f-4f65-42c6-b005-242550b8b8bf',
            occurred_date=1725512986000, 
            category=STRIKE_CATEGORY.OTHER,
            description='testing creating a strike',
        )
        
        new_strike= CreateStrikeViewmodel(strike=strike, case_number=1)

        expected = {
            'strike_id': 'n4o5p6q7-r8s9-0123-4567-890123nopqtu',
            'owner_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            'target_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0', 
            'applier_user_id': '3b07232f-4f65-42c6-b005-242550b8b8bf',
            'occurred_date': 1725512986000, 
            'category': STRIKE_CATEGORY.OTHER,
            'description': 'testing creating a strike',
            'case_number': 1,
            'message': 'Strike was created successfully and hours were reset'
        }

        assert new_strike.to_dict() == expected