import json
from src.modules.create_project.app.create_project_presenter import lambda_handler


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
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
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
            "body": '{"code":"DM","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_RA":"21021031","scrum_RA":"17033730","start_date":1649955600000,"members":["21021031","17033730"],"photos":["https://i.imgur.com/7QF7uCk.png"]}',
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
                'po_RA': '21021031',
                'scrum_RA': '17033730',
                'start_date': 1649955600000,
                'members': ['17033730','21021031'],
                'photos': [
                    'https://i.imgur.com/7QF7uCk.png'
                ]
            },
            'message': 'the project was created'
        }
        assert response["statusCode"] == 201
        assert json.loads(response["body"]) == expected

    def test_create_project_presenter_with_missing_photos(self):
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
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
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
            "body": '{"code":"DM","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_RA":"21021031","scrum_RA":"17033730","start_date":1649955600000,"members":["21021031","17033730"]}',
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
                'po_RA': '21021031',
                'scrum_RA': '17033730',
                'start_date': 1649955600000,
                'members': ['17033730','21021031'],
                'photos': []
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
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
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
            "body": '{"name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_RA":"21021031","scrum_RA":"17033730","start_date":1649955600000,"members":["21021031","17033730"],"photos":["https://i.imgur.com/7QF7uCk.png"]}',
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
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
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
            "body": '{"code":"DM","name":"DevMedias","description":"Projeto que calcula a média de notas e quanto um aluno precisa tirar para passar de ano","po_RA":"21021031","scrum_RA":"não tem","start_date":1649955600000,"members":["21021031","17033730"],"photos":["https://i.imgur.com/7QF7uCk.png"]}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field scrum_RA is not valid"
        
    # def test_create_project_presenter_duplicated_item(self):