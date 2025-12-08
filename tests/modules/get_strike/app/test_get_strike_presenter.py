import json
import os
os.environ['STAGE'] = 'TEST'
from src.modules.get_strike.app.get_strike_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.strike_repository_mock import StrikeRepositoryMock

class Test_GetStrikePresenter:

    repo_member = MemberRepositoryMock()
    repo_strike = StrikeRepositoryMock()

    requester_user = repo_member.members[0]
    target_strike = repo_strike.strikes[0]

    def test_get_strike_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/get_strike",
            "rawQueryString": "",
            "headers": {
                "header1": "value1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authorizer": {
                    "claims": {
                        "sub": self.requester_user.user_id,
                        "name": self.requester_user.name,
                        "email": self.requester_user.email,
                        "custom:isMaua": True
                    }
                },
                "http": {
                    "method": "POST", # Geralmente POST se enviamos body, ou GET se for queryString
                    "path": "/get_strike",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "stage": "$default",
                "timeEpoch": 1583348638390
            },
            # Passando o strike_id no body como JSON string
            "body": json.dumps({"strike_id": self.target_strike.strike_id}),
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200

        body_dict = json.loads(response["body"])
        assert body_dict["strike"]["strike_id"] == self.target_strike.strike_id

    def test_get_strike_presenter_missing_id(self):
        event = {
            "version": "2.0",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": self.requester_user.user_id,
                        "name": self.requester_user.name,
                        "email": self.requester_user.email,
                        "custom:isMaua": True
                    }
                },
                "http": {"method": "POST"}
            },
            "body": json.dumps({}), # Body vazio
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400

    def test_get_strike_presenter_unauthorized(self):
        event = {
            "version": "2.0",
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "user-inexistente",
                        "name": "Ghost",
                        "email": "ghost@test.com",
                        "custom:isMaua": True
                    }
                },
                "http": {"method": "POST"}
            },
            "body": json.dumps({"strike_id": self.target_strike.strike_id}),
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 403