import json
from src.modules.update_project.app.update_project_presenter import lambda_handler
from src.shared.infra.repositories.action_repository_mock import ActionRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

first_member = MemberRepositoryMock().members[0]
class TestUpdateProjectPresenter:

    def test_update_project_presenter(self):
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
            "body": '{"code": "PT", "new_name": "Projeto portfolio", "new_description": "Projeto para o portfolio", "new_po_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "new_scrum_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "new_photo": "https://i.imgur.com/gHoRKJU.png", "new_members_user_ids": ["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event=event, context=None)
        
        assert response['statusCode'] == 200
        assert json.loads(response['body'])['message'] == 'the project was updated'

    def test_update_project_without_code(self):
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
            "body": '{"new_name": "Projeto portfolio", "new_description": "Projeto para o portfolio", "new_po_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "new_scrum_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "new_photo": "https://i.imgur.com/gHoRKJU.png", "new_members_user_ids": ["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event=event, context=None)
        
        assert response['statusCode'] == 400
        assert json.loads(response['body']) == 'Field code is missing'

    def test_update_project_presenter_wrong_type_parameter(self):
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
            "body": '{"code": 25, "new_name": "Projeto portfolio", "new_description": "Projeto para o portfolio", "new_po_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "new_scrum_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "new_photo": "https://i.imgur.com/gHoRKJU.png", "new_members_user_ids": ["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event=event, context=None)
        
        assert response['statusCode'] == 400
        assert json.loads(response['body']) == 'Field code is not valid'
        
    def test_update_project_presenter_entity_error(self):
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
            "body": '{"code": "PORT", "new_name": "Projeto portfolio", "new_description": "Projeto para o portfolio", "new_po_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "new_scrum_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "new_photo": "https://i.imgur.com/gHoRKJU.png", "new_members_user_ids": ["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event=event, context=None)
        
        assert response['statusCode'] == 400
        assert json.loads(response['body']) == 'Field code is not valid'
        
    def test_update_project_presenter_entity_not_found(self):
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
            "body": '{"code": "RR", "new_name": "Projeto portfolio", "new_description": "Projeto para o portfolio", "new_po_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "new_scrum_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "new_photo": "https://i.imgur.com/gHoRKJU.png", "new_members_user_ids": ["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event=event, context=None)
        
        assert response['statusCode'] == 404
        assert json.loads(response['body']) == 'No items found for project'

    def test_update_project_presenter_requester_user_missing(self):
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
            "body": '{"code": "PT", "new_name": "Projeto portfolio", "new_description": "Projeto para o portfolio", "new_po_user_id": "93bc6ada-c0d1-7054-66ab-e17414c48ae3", "new_scrum_user_id": "51ah5jaj-c9jm-1345-666ab-e12341c14a3", "new_photo": "https://i.imgur.com/gHoRKJU.png", "new_members_user_ids": ["93bc6ada-c0d1-7054-66ab-e17414c48ae3", "51ah5jaj-c9jm-1345-666ab-e12341c14a3"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event=event, context=None)
        
        assert response['statusCode'] == 400
        assert json.loads(response['body']) == 'Field requester_user is missing'