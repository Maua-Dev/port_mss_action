import json
from src.modules.delete_strike.app.delete_strike_controller import DeleteStrikeController
from src.modules.delete_strike.app.delete_strike_presenter import lambda_handler
from src.modules.delete_strike.app.delete_strike_usecase import DeleteStrikeUseCase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock

class Test_DeleteStrikePresenter:
    def test_delete_strike_presenter_success(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/delete-strike",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                        "name": "Ryuske",
                        "email": "ryuske@gmail.com",
                        "custom:isMaua": True
                    }
                }
            },
            "body": '{"strike_id" : "a1b2c3d4-e5f6-7890-1234-567890abcdef"}'
        }

        response = lambda_handler(event, None)

        expected_body = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1764622800000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected_body


    def test_delete_strike_presenter_missing_parameters(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/delete-strike",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                        "name": "Ryuske",
                        "email": "ryuske@gmail.com",
                        "custom:isMaua": True
                    }
                }
            },
            "body": "{}"
        }

        response = lambda_handler(event, None)

        expected_body = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1756987200000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field strike_id is missing"


    def test_delete_strike_presenter_entity_error(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/delete-strike",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                        "name": "Ryuske",
                        "email": "ryuske@gmail.com",
                        "custom:isMaua": True
                    }
                }
            },
            "body": '{"strike_id" : "a1b2c3d4-e5f-7890-1234-567890abcdef"}'
        }

        response = lambda_handler(event, None)

        expected_body = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1756987200000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field strike_id is not valid"


    def test_delete_strike_presenter_not_found(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/delete-strike",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                        "name": "Ryuske",
                        "email": "ryuske@gmail.com",
                        "custom:isMaua": True
                    }
                }
            },
            "body": '{"strike_id" : "a1b2c3d4-e5g6-7890-1234-567890abcdef"}'
        }

        response = lambda_handler(event, None)

        expected_body = {
            "strike": {
                "strike_id": "a1b2c3d4-e5g6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1756987200000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for strike_id"


    def test_delete_strike_presenter_forbidden(self):

        repo = StrikeRepositoryMock() # novo repo isolado
        repo_member = MemberRepositoryMock()  # novo repo isolado
        usecase = DeleteStrikeUseCase(repo=repo, repo_member=repo_member)
        controller = DeleteStrikeController(usecase=usecase)

        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/delete-strike",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0",
                        "name": "Fernandao Presidas",
                        "email": "fernandao@gmail.com",
                        "custom:isMaua": True
                    }
                }
            },
            "body": '{"strike_id" : "b2c3d4e5-f6g7-8901-2345-678901bcdefg"}'
        }

        response = lambda_handler(event, None)

        expected_body = {
            "strike": {
                "strike_id": "b2c3d4e5-f6g7-8901-2345-678901bcdefg",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7gh5yf5H-857H-1234-75hng-94832hvng1s",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1756987200000,
                "category": "LACK_OF_COMMITMENT",
                "description": "Ausência injustificada em projeto crítico",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert response["statusCode"] == 403
        assert json.loads(response["body"]) == "That action is forbidden for this type of user"

    def test_delete_strike_presenter_unregistered_user(self):

        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/delete-strike",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3b07232f-4f65-42c6-b005-242550b8b8dd",
                        "name": "Carlinhos Miao",
                        "email": "carlinhosmiao@gmail.com",
                        "custom:isMaua": True
                    }
                }
            },
            "body": '{"strike_id" : "a1b2c3d4-e5f6-7890-1234-567890abcdef"}'
        }

        response = lambda_handler(event, None)

        expected_body = {
            "strike": {
                "strike_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "owner_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "target_user_id": "7465hvnb-143g-1675-86HnG-75hgnFbcg36",
                "applier_user_id": "3b07232f-4f65-42c6-b005-242550b8b8bf",
                "occurred_date": 1756987200000,
                "category": "MISCONDUCT",
                "description": "Comportamento inadequado durante reunião",
                "is_valid": True
            },
            "message": "the strike was deleted successfully"
        }

        assert response["statusCode"] == 403
        assert json.loads(response["body"]) == "That user is not registered"