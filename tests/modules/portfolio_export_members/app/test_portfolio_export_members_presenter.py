import json
from src.modules.portfolio_export_members.app.portfolio_export_members_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

repo_mock = MemberRepositoryMock()


class Test_PortfolioExportMembersPresenter:

    def _build_event(self):
        return {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "GET",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": None,
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

    def test_portfolio_export_members_presenter(self):
        response = lambda_handler(self._build_event(), None)

        assert response["statusCode"] == 200
        body = json.loads(response["body"])

        assert "homeCarousel" in body
        assert "quoteCarousel" in body
        assert "memberCarousel" in body
        assert isinstance(body["homeCarousel"], list)
        assert len(body["homeCarousel"]) > 0

    def test_portfolio_export_members_presenter_response_shape(self):
        response = lambda_handler(self._build_event(), None)
        body = json.loads(response["body"])

        assert len(body["homeCarousel"]) == len(repo_mock.members)
        assert len(body["quoteCarousel"]) == len(repo_mock.members)
        assert len(body["memberCarousel"]) == len(repo_mock.members)

        assert set(body["homeCarousel"][0].keys()) == {"name", "photoPath", "area"}
        assert set(body["quoteCarousel"][0].keys()) == {"name", "quote", "photoPath", "role"}
        assert set(body["memberCarousel"][0].keys()) == {"name", "photoPath", "email", "role", "phone"}
