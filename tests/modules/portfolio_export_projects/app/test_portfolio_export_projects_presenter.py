import json
from src.modules.portfolio_export_projects.app.portfolio_export_projects_presenter import lambda_handler
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock

repo_mock = ActionRepositoryMock()


class Test_PortfolioExportProjectsPresenter:

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

    def test_portfolio_export_projects_presenter(self):
        response = lambda_handler(self._build_event(), None)

        assert response["statusCode"] == 200
        body = json.loads(response["body"])

        assert "projects" in body
        assert isinstance(body["projects"], list)
        assert len(body["projects"]) > 0

        first_project = body["projects"][0]
        assert set(first_project.keys()) == {"code", "name", "description", "photo"}

    def test_portfolio_export_projects_presenter_response_shape(self):
        response = lambda_handler(self._build_event(), None)
        body = json.loads(response["body"])

        assert len(body["projects"]) == len(repo_mock.projects)

        for index, project in enumerate(repo_mock.projects):
            exported = body["projects"][index]
            assert exported["code"] == project.code
            assert exported["name"] == project.name
            assert exported["description"] == project.description
            assert exported["photo"] == (project.photo if project.photo is not None else "")
            assert set(exported.keys()) == {"code", "name", "description", "photo"}
