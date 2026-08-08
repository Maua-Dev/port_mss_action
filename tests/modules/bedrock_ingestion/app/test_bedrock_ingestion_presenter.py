import json
from unittest.mock import patch, MagicMock
from src.modules.bedrock_ingestion.app.bedrock_ingestion_presenter import lambda_handler

class Test_BedrockIngestionPresenter:
    @patch('src.modules.bedrock_ingestion.app.bedrock_ingestion_presenter.controller')
    def test_bedrock_ingestion_presenter(self, mock_controller):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = {
            "data": {
                "job_id": "mock_job_id",
                "status": "STARTING"
            },
            "message": "Bedrock ingestion started successfully"
        }
        mock_response.headers = None
        mock_controller.return_value = mock_response
        
        event = {
            "source": "aws.s3",
            "detail-type": "Object Created",
            "detail": {
                "bucket": {
                    "name": "mock_bucket"
                },
                "object": {
                    "key": "mock_object.pdf"
                }
            }
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        assert body["data"]["job_id"] == "mock_job_id"
        assert body["message"] == "Bedrock ingestion started successfully"
        
    def test_bedrock_ingestion_presenter_invalid_source(self):
        event = {
            "source": "aws.ec2",
            "detail-type": "Object Created"
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body == "Invalid event source. Expected S3 Object Created event from EventBridge."
        
    def test_bedrock_ingestion_presenter_invalid_detail_type(self):
        event = {
            "source": "aws.s3",
            "detail-type": "Bucket Created"
        }
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body == "Invalid event source. Expected S3 Object Created event from EventBridge."
