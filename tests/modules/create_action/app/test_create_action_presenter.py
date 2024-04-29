import json
from src.modules.create_action.app.create_action_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


member = MemberRepositoryMock().members[0]

class Test_CreateActionPresenter:

    

    def test_create_action_presenter(self):
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
                            "sub": member.user_id, 
                            "name": member.name,
                            "email": member.email,
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
            "body": '{"start_date":1634526000000,"title":"Teste","end_date":1634533200000, "duration":7200000, "project_code":"MF","associated_members_user_ids":["7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"stack_tags":["BACKEND"],"action_type_tag":"CODE", "story_id":100}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        assert json.loads(response["body"])["action"]["start_date"] == 1634526000000
        assert json.loads(response["body"])["action"]["end_date"] == 1634533200000
        assert json.loads(response["body"])["action"]["duration"] == 7200000
        assert json.loads(response["body"])["action"]["story_id"] == 100
        assert json.loads(response["body"])["action"]["title"] == 'Teste'
        assert json.loads(response["body"])["action"]["description"] == None
        assert json.loads(response["body"])["action"]["project_code"] == 'MF'
        assert json.loads(response["body"])["action"]["associated_members_user_ids"] == ['7465hvnb-143g-1675-86HnG-75hgnFbcg36']
        assert json.loads(response["body"])["action"]["stack_tags"] == ['BACKEND']
        assert json.loads(response["body"])["action"]["action_type_tag"] == 'CODE'
        assert json.loads(response["body"])["action"]["is_valid"] == True
        assert json.loads(response["body"])["action"]["user_id"] == '93bc6ada-c0d1-7054-66ab-e17414c48ae3'
        assert json.loads(response["body"])["message"] == 'the action was created'
        
    def test_create_action_presenter_missing_parameters(self):
        
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
                            "sub": member.user_id, 
                            "name": member.name,
                            "email": member.email,
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
            "body": '{"start_date":1634526000000,"end_date":1634533200000, "duration":7200000, "project_code":"MF","associated_members_user_ids":["7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"stack_tags":["BACKEND"],"action_type_tag":"CODE", "story_id":100}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Field title is missing'
        
    def test_create_action_presenter_entity_error(self):
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
                            "sub": '25', 
                            "name": member.name,
                            "email": member.email,
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
            "body": '{"start_date":1634526000000,"title":"Teste","end_date":1634533200000, "duration":7200000, "project_code":"MF","associated_members_user_ids":["7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"stack_tags":["BACKEND"],"action_type_tag":"CODE", "story_id":100}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Field user_id is not valid'
        
    def test_create_action_presenter_no_items_found(self):
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
                            "sub": "ab83jBnh-997H-1010-10god-914gHy46tBh", 
                            "name": member.name,
                            "email": member.email,
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
            "body": '{"start_date":1634526000000,"title":"Teste","end_date":1634533200000, "duration":7200000, "project_code":"MF","associated_members_user_ids":["7465hvnb-143g-1675-86HnG-75hgnFbcg36"],"stack_tags":["BACKEND"],"action_type_tag":"CODE", "story_id":100}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'That user is not registered'