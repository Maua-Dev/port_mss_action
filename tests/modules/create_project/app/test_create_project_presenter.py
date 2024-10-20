import json
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.modules.create_project.app.create_project_presenter import lambda_handler


first_member = MemberRepositoryMock().members[0]
class Test_CreateProjectPresenter:
    def test_create_project_presenter(self):
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
            "body": '{"code":"DM","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_user_id":"5f55f6a5-a66e-4fff-9faf-72cd478bd5a0","scrum_user_id":"5f55f6a5-a66e-4fff-9faf-72cd478bd5a0","start_date":1649955600000,"members_user_ids":["93bc6ada-c0d1-7054-66ab-e17414c48ae3","7465hvnb-143g-1675-86HnG-75hgnFbcg36","5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"],"photo":"https://i.imgur.com/7QF7uCk.png"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        expected = {
            'project': {
                'code': 'DM',
                'name': 'DevMedias',
                'description': 'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'scrum_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'start_date': 1649955600000,
                'members_user_ids': ['5f55f6a5-a66e-4fff-9faf-72cd478bd5a0','7465hvnb-143g-1675-86HnG-75hgnFbcg36','93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                'photo': 'https://i.imgur.com/7QF7uCk.png'

            },
            'message': 'the project was created'
        }
        assert response["statusCode"] == 201
        assert json.loads(response["body"]) == expected

    def test_create_project_presenter_with_missing_photo(self):
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
            "body": '{"code":"DS","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_user_id":"5f55f6a5-a66e-4fff-9faf-72cd478bd5a0","scrum_user_id":"5f55f6a5-a66e-4fff-9faf-72cd478bd5a0","start_date":1649955600000,"members_user_ids":["93bc6ada-c0d1-7054-66ab-e17414c48ae3","7465hvnb-143g-1675-86HnG-75hgnFbcg36","5f55f6a5-a66e-4fff-9faf-72cd478bd5a0"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        expected = {
            'project': {
                'code': 'DS',
                'name': 'DevMedias',
                'description': 'Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano',
                'po_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'scrum_user_id': '5f55f6a5-a66e-4fff-9faf-72cd478bd5a0',
                'start_date': 1649955600000,
                'members_user_ids': ['5f55f6a5-a66e-4fff-9faf-72cd478bd5a0','7465hvnb-143g-1675-86HnG-75hgnFbcg36','93bc6ada-c0d1-7054-66ab-e17414c48ae3'],
                'photo': None
            },
            'message': 'the project was created'
        }
        assert response["statusCode"] == 201
        assert json.loads(response["body"]) == expected
        
    def test_create_project_presenter_missing_parameters(self):
        
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
            "body": '{"name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3","scrum_user_id":"7465hvnb-143g-1675-86HnG-75hgnFbcg36","start_date":1649955600000,"members_user_ids":["93bc6ada-c0d1-7054-66ab-e17414c48ae3","7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"photo":"https://i.imgur.com/7QF7uCk.png"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field code is missing"
        
    def test_create_project_presenter_entity_error(self):
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
            "body": '{"code":"DM","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3","scrum_user_id":"não tem","start_date":1649955600000,"members_user_ids":["93bc6ada-c0d1-7054-66ab-e17414c48ae3","7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"photo":"https://i.imgur.com/7QF7uCk.png"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field scrum_user_id is not valid"
        
    def test_create_project_presenter_requester_user_missing(self):
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
            "body": '{"code":"DM","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_user_id":"93bc6ada-c0d1-7054-66ab-e17414c48ae3","scrum_user_id":"não tem","start_date":1649955600000,"members_user_ids":["93bc6ada-c0d1-7054-66ab-e17414c48ae3","7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"photo":"https://i.imgur.com/7QF7uCk.png"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field requester_user is missing"
