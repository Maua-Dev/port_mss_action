import json
from src.modules.update_action.app.update_action_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

first_member = MemberRepositoryMock().members[0]
class Test_UpdateActionPresenter:
    def test_update_action_presenter(self):
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
            "body": '{"action_id": "5f4f13df-e7d3-4a10-9219-197ceae9e3f0","new_start_date":1634526000000,"new_story_id":100,"new_associated_members_user_ids":["32ah5jaj-c9jm-1345-666ab-e12341c14a3"],"new_title":"Teste","new_end_date":1634536800000,"new_project_code":"MF","new_stack_tags":["BACKEND"],"new_action_type_tag":"CODE","new_duration":1000000, "new_is_valid": false}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == 'the action was updated'
        assert json.loads(response["body"])["action"]["user_id"] == "6f5g4h7J-876j-0098-123hb-hgb567fy4hb"
        assert json.loads(response["body"])["action"]["start_date"] == 1634526000000
        assert json.loads(response["body"])["action"]["end_date"] == 1634536800000
        assert json.loads(response["body"])["action"]["story_id"] == 100
        assert json.loads(response["body"])["action"]["associated_members_user_ids"] == ['32ah5jaj-c9jm-1345-666ab-e12341c14a3', "6f5g4h7J-876j-0098-123hb-hgb567fy4hb"]
        assert json.loads(response["body"])["action"]["title"] == 'Teste'
        assert json.loads(response["body"])["action"]["project_code"] == 'MF'
        assert json.loads(response["body"])["action"]["stack_tags"] == ['BACKEND']
        assert json.loads(response["body"])["action"]["action_type_tag"] == 'CODE'
        assert json.loads(response["body"])["action"]["duration"] == 1000000
        
    def test_update_action_presenter_missing_parameters(self):
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
            "body": '{"new_user_id":"51ah5jaj-c9jm-1345-666ab-e12341c14a3","new_start_date":1634526000000,"new_story_id":100,"new_associated_members_user_ids":["19015jaj-c9jm-1345-666ab-e12341c14a37311"],"new_title":"Teste","new_end_date":1634536800000,"new_project_code":"MF","new_stack_tags":["BACKEND"],"new_action_type_tag":"CODE","new_duration":1000000}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Field action_id is missing'
        
    def test_update_action_presenter_wrong_type_parameter(self):
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
            "body": '{"action_id": 777,"new_start_date":1634526000000,"new_story_id":100,"new_associated_members_user_ids":["19015jaj-c9jm-1345-666ab-e12341c14a37311"],"new_title":"Teste","new_end_date":1634536800000,"new_project_code":"MF","new_stack_tags":["BACKEND"],"new_action_type_tag":"CODE","new_duration":1000000}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Field action_id isn\'t in the right type.\n Received: <class \'int\'>.\n Expected: str'
        
    def test_update_action_presenter_entity_error(self):
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
            "body": '{"action_id": "nao-sou-um-uuid","new_start_date":1634526000000,"new_story_id":100,"new_associated_members_user_ids":["19015jaj-c9jm-1345-666ab-e12341c14a37311"],"new_title":"Teste","new_end_date":1634536800000,"new_project_code":"MF","new_stack_tags":["BACKEND"],"new_action_type_tag":"CODE","new_duration":1000000}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Field action_id is not valid'
        
    def test_update_action_presenter_no_items_found(self):
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
            "body": '{"action_id": "5fcf13df-e7d3-4a10-9219-197ceae9e3f0","new_start_date":1634526000000,"new_story_id":100,"new_associated_members_user_ids":["32ah5jaj-c9jm-1345-666ab-e12341c14a3"],"new_title":"Teste","new_end_date":1634536800000,"new_project_code":"MF","new_stack_tags":["BACKEND"],"new_action_type_tag":"CODE","new_duration":1000000, "new_is_valid": false}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        print(response)
        
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == 'No items found for action'