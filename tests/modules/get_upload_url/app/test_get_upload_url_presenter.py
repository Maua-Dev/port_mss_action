import json
import os
import pytest
from src.modules.get_upload_url.app.get_upload_url_presenter import lambda_handler

class Test_GetUploadUrlPresenter:
    @pytest.mark.skip(reason="Requires MinIO running locally in Docker")
    def test_get_upload_url_presenter(self):
        os.environ["STAGE"] = "TEST"
        
        event = {
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "93bc6ada-c0d1-7054-66ab-e17414c48ae3",
                        "name": "Vitor Guirão MPNTM",
                        "email": "vsoller.devmaua@gmail.com",
                        "custom:isMaua": "true"
                    }
                }
            },
            "queryStringParameters": {
                "file_name": "test_integration_doc.pdf"
            }
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        
        upload_url = body.get("upload_url")
        print("BODY:", body)
        assert upload_url is not None
        
        print("\n\n" + "="*80)
        print("PRESIGNED URL GENERATED FOR POSTMAN:")
        print(upload_url)
        print("="*80 + "\n\n")
