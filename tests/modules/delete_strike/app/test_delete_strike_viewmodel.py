from src.modules.delete_strike.app.delete_strike_viewmodel import DeleteStrikeViewModel
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY


class Test_DeleteStrikeViewModel:
    def test_delete_strike_viewmodel(self):
        strike = Strike(
            strike_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
            applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
            occurred_date=1703980800000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Comportamento inadequado durante reunião"
        )

        viewmodel = DeleteStrikeViewModel(strike).to_dict()

        expected = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1703980800000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert viewmodel == expected

    def test_delete_strike_viewmodel_without_description(self):
        strike = Strike(
            strike_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
            applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
            occurred_date=1703980800000,
            category=STRIKE_CATEGORY.LACK_OF_COMMITMENT
        )

        viewmodel = DeleteStrikeViewModel(strike).to_dict()

        expected = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1703980800000,
                "category": "LACK_OF_COMMITMENT",
                "description": None,
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert viewmodel == expected

from src.modules.delete_strike.app.delete_strike_viewmodel import DeleteStrikeViewModel
from src.shared.domain.entities.strike import Strike
from src.shared.domain.enums.strike_category import STRIKE_CATEGORY


class Test_DeleteStrikeViewModel:
    def test_delete_strike_viewmodel(self):
        strike = Strike(
            strike_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
            applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
            occurred_date=1703980800000,
            category=STRIKE_CATEGORY.MISCONDUCT,
            description="Comportamento inadequado durante reunião"
        )

        viewmodel = DeleteStrikeViewModel(strike).to_dict()

        expected = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1703980800000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert viewmodel == expected

    def test_delete_strike_viewmodel_without_description(self):
        strike = Strike(
            strike_id="a1b2c3d4-e5f6-7890-1234-567890abcdef",
            owner_user_id="93bc6ada-c0d1-7054-66ab-e17414c48ae3",
            target_user_id="7465hvnb-143g-1675-86HnG-75hgnFbcg36",
            applier_user_id="3b07232f-4f65-42c6-b005-242550b8b8bf",
            occurred_date=1703980800000,
            category=STRIKE_CATEGORY.LACK_OF_COMMITMENT
        )

        viewmodel = DeleteStrikeViewModel(strike).to_dict()

        expected = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1703980800000,
                "category": "LACK_OF_COMMITMENT",
                "description": None,
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert viewmodel == expected