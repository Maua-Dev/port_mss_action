import json
from src.modules.update_member.app.update_member_presenter import lambda_handler


class Test_UpdateMemberPresenter:
    def test_update_member_presenter(self):
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
                            "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                            "name": "Lucas Duez",
                            "email": "lucas.santos@gmail.com",
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
            "body": '{"ra": "21017310","new_name":"Joao Branco","new_email_dev":"jbranco.devmaua@gmail.com","new_role":"HEAD","new_stack":"BACKEND","new_year":3,"new_cellphone":"11991152348","new_course":"ECM","new_active":"ACTIVE"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["message"] == 'the member was updated'
        assert json.loads(response["body"])["member"]["name"] == "Joao Branco"
        assert json.loads(response["body"])["member"]["email_dev"] == "jbranco.devmaua@gmail.com"
        assert json.loads(response["body"])["member"]["ra"] == "21017310"
        assert json.loads(response["body"])["member"][ "role"] == "HEAD"
        assert json.loads(response["body"])["member"][ "stack"] == "BACKEND"
        assert json.loads(response["body"])["member"]["year"] == 3
        assert json.loads(response["body"])["member"]["cellphone"] == "11991152348"
        assert json.loads(response["body"])["member"]["course"] == "ECM"
        assert json.loads(response["body"])["member"]["hired_date"] == 1634576165000
        assert json.loads(response["body"])["member"]["active"] == "ACTIVE"
        assert json.loads(response["body"])["member"]["deactivated_date"] == None      
 