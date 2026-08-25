import json

from src.modules.get_hours_chart.app.get_hours_chart_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

director = MemberRepositoryMock().members[0]
dev = next(m for m in MemberRepositoryMock().members if m.user_id == "7gh5yf5H-857H-1234-75hng-94832hvng1s")


def make_event(user, query_string_parameters=None):
    return {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/my/path",
        "rawQueryString": "",
        "cookies": [],
        "headers": {},
        "queryStringParameters": query_string_parameters,
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "claims": {
                    "sub": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "custom:isMaua": True
                }
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
        "body": '{}',
        "pathParameters": None,
        "isBase64Encoded": None,
        "stageVariables": None
    }


class Test_GetHoursChartPresenter:
    def test_get_hours_chart_presenter(self):
        event = make_event(director, query_string_parameters={"start_date": "1637046000000", "end_date": "1690046000000"})

        response = lambda_handler(event=event, context=None)

        assert response['statusCode'] == 200
        body = json.loads(response['body'])
        assert body['message'] == 'the hours chart data was retrieved'
        assert body['areas'] == ['BACKEND', 'FRONTEND', 'INFRA', 'UX_UI', 'BUSINESS', 'INTERNAL', 'RH']
        assert body['hours_by_project']['MF'] == 17255.56

    def test_get_hours_chart_presenter_no_query_params(self):
        event = make_event(director, query_string_parameters=None)

        response = lambda_handler(event=event, context=None)

        assert response['statusCode'] == 200

    def test_get_hours_chart_presenter_forbidden(self):
        event = make_event(dev)

        response = lambda_handler(event=event, context=None)

        assert response['statusCode'] == 403

    def test_get_hours_chart_presenter_user_not_found(self):
        event = make_event(director)
        event["requestContext"]["authorizer"] = {
            "iam": {
                "accessKey": "AKIA...",
                "accountId": "111122223333",
                "callerId": "AIDA...",
                "cognitoIdentity": None,
                "principalOrgId": None,
                "userArn": "arn:aws:iam::111122223333:user/example-user",
                "userId": "AIDA..."
            }
        }

        response = lambda_handler(event=event, context=None)

        assert response['statusCode'] == 400
        assert json.loads(response['body']) == 'Field requester_user is missing'