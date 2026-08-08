import json
from unittest import mock
from src.modules.create_strike.app.create_strike_presenter import lambda_handler


class Test_CreateStrikePresenter:
    def test_create_strike_presenter_case_0(self):
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
                            "sub":"51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                            "name":"Joao Branco",
                            "email":"jbranco@gmail.com",
                            "custom:isMaua":True
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
            "body": '{"owner_user_id" : "51ah5jaj-c9jm-1345-666ab-e12341c14a3","target_user_id": "5f55f6a5-a66e-4fff-9faf-72cd478bd5a0", "occurred_date": 1725512986000, "category": "OTHER","description": "testing creating a strike"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        expected = {
            'strike_id': json.loads(response['body'])['strike_id'],
            'owner_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            'target_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
            'applier_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            'occurred_date': 1725512986000,
            'category': 'OTHER',
            'description': 'testing creating a strike',
            'case_number': 0,
            'message': 'Strike was created successfully'
        }

        assert response['statusCode'] == 201
        assert json.loads(response['body']) == expected

    def test_create_strike_presenter_case_1(self):
        from src.modules.create_strike.app.create_strike_presenter import repo
        # Remove one strike to make it exactly 3 strikes before the request
        deleted_strike = repo.delete_strike("i9j0k1l2-m3n4-5678-9012-345678ijklmn")

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
                            "sub":"51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                            "name":"Joao Branco",
                            "email":"jbranco@gmail.com",
                            "custom:isMaua":True
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
            "body": '{"owner_user_id" : "51ah5jaj-c9jm-1345-666ab-e12341c14a3","target_user_id": "6f5g4h7J-876j-0098-123hb-hgb567fy4hb", "occurred_date": 1764622800000, "category": "OTHER","description": "testing creating a strike"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        expected = {
            'strike_id': json.loads(response['body'])['strike_id'],
            'owner_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            'target_user_id': '6f5g4h7J-876j-0098-123hb-hgb567fy4hb',
            'applier_user_id': '51ah5jaj-c9jm-1345-666ab-e12341c14a3',
            'occurred_date': 1764622800000,
            'category': 'OTHER',
            'description': 'testing creating a strike',
            'case_number': 1,
            'message': 'Strike was created successfully, hours were reset and an Email was sent to Directors and Heads'
        }

        assert response['statusCode'] == 201
        assert json.loads(response['body']) == expected

        # cleanup
        repo.delete_strike(expected["strike_id"])
        if deleted_strike:
            repo.create_strike(deleted_strike)

    def test_create_strike_presenter_case_2(self):
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
                            "sub":"51ah5jaj-c9jm-1345-666ab-e12341c14a3",
                            "name":"Joao Branco",
                            "email":"jbranco@gmail.com",
                            "custom:isMaua":True
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
            "body": '{"owner_user_id" : "51ah5jaj-c9jm-1345-666ab-e12341c14a3","target_user_id": "75648hbr-184n-1985-91han-7ghn4HgF182", "occurred_date": 1725512986000, "category": "OTHER","description": "testing creating a strike"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response['statusCode'] == 403
        assert json.loads(response['body']) == "Member has already reached the strike limit for this semester"