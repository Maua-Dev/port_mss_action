import json
from src.modules.create_member.app.create_member_presenter import lambda_handler
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK

class Test_CreateMemberPresenter:
    def test_create_member_presenter(self):
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
                     "claims":{
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão MPNTM",
                "email": "vsoller@airubio.com",
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
            "body": '{"email_dev":"vsoller.devmaua@gmail.com","ra":"21017315","role":"DIRECTOR","stack":"INFRA","year":1,"cellphone":"11991758098","course":"ECA","hired_date":1614567601000}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        assert json.loads(response["body"])['member']['name'] == 'Vitor Guirão MPNTM'
        assert json.loads(response["body"])['member']['email_dev'] == "vsoller.devmaua@gmail.com"
        assert json.loads(response["body"])['member']['email'] == "vsoller@airubio.com"
        assert json.loads(response["body"])['member']['ra'] == "21017315"
        assert json.loads(response["body"])['member']['role'] == ROLE.DIRECTOR.value
        assert json.loads(response["body"])['member']['stack'] == STACK.INFRA.value
        assert json.loads(response["body"])['member']['year'] == 1
        assert json.loads(response["body"])['member']['cellphone'] == "11991758098"
        assert json.loads(response["body"])['member']['course'] == COURSE.ECA.value
        assert json.loads(response["body"])['member']['hired_date'] == 1614567601000
        assert json.loads(response["body"])['member']['active'] == ACTIVE.ACTIVE.value
        assert json.loads(response["body"])['member']['user_id'] == "13bc6ada-c0d1-7054-66ab-e17414c48ae3"
        assert json.loads(response["body"])['member']['deactivated_date'] == None   
        assert json.loads(response["body"])["message"] == 'the member was created'

    def test_create_user_invalid_id(self):
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
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "ABC",
                            "name": "Vitinho Molhas",
                            "email": "molhas@maua.br",
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
            "body": "Hello from client!",
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400