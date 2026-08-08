from unittest.mock import MagicMock
from src.modules.bedrock_ingestion.app.bedrock_ingestion_controller import BedrockIngestionController
from src.shared.helpers.errors.usecase_errors import DataIngestionError

class Test_BedrockIngestionController:
    def test_bedrock_ingestion_controller(self):
        usecase = MagicMock()
        usecase.return_value = {
            "job_id": "mock_job_id",
            "status": "STARTING"
        }
        controller = BedrockIngestionController(usecase)
        
        request = {
            "detail": {
                "bucket": {
                    "name": "mock_bucket"
                },
                "object": {
                    "key": "mock_object.pdf"
                }
            }
        }
        
        response = controller(request)
        
        assert response.status_code == 200
        assert response.body["data"] == {
            "job_id": "mock_job_id",
            "status": "STARTING"
        }
        assert response.body["message"] == "Bedrock ingestion started successfully"
        usecase.assert_called_once_with("mock_bucket", "mock_object.pdf")
        
    def test_bedrock_ingestion_controller_missing_bucket(self):
        usecase = MagicMock()
        controller = BedrockIngestionController(usecase)
        
        request = {
            "detail": {
                "object": {
                    "key": "mock_object.pdf"
                }
            }
        }
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field bucket name ou object key is missing"
        
    def test_bedrock_ingestion_controller_missing_object_key(self):
        usecase = MagicMock()
        controller = BedrockIngestionController(usecase)
        
        request = {
            "detail": {
                "bucket": {
                    "name": "mock_bucket"
                }
            }
        }
        
        response = controller(request)
        
        assert response.status_code == 400
        assert response.body == "Field bucket name ou object key is missing"
        
    def test_bedrock_ingestion_controller_usecase_error(self):
        usecase = MagicMock()
        usecase.side_effect = DataIngestionError("AWS Error")
        controller = BedrockIngestionController(usecase)
        
        request = {
            "detail": {
                "bucket": {
                    "name": "mock_bucket"
                },
                "object": {
                    "key": "mock_object.pdf"
                }
            }
        }
        
        response = controller(request)
        
        assert response.status_code == 503
        assert response.body == "Error starting bedrock ingestion: AWS Error"
