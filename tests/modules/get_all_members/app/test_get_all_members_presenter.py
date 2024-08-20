import json
from src.modules.get_all_members.app.get_all_members_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

first_member = MemberRepositoryMock().members[0]
class Test_GetAllMembersPresenter:

    def test_get_all_members_presenter(self):
        event = {
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
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": first_member.user_id,
                            "name": first_member.name,
                            "email": first_member.email,
                            "custom:isMaua": True
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
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
            "body": '{"start_date":1624576165000,"end_date":1690046000000}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event=event, context=None)

        assert response['statusCode'] == 200
        assert json.loads(response['body'])['message'] == 'the members were retrieved'