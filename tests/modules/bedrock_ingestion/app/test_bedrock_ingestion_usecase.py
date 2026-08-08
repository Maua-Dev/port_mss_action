import pytest
from unittest.mock import MagicMock, patch
from src.modules.bedrock_ingestion.app.bedrock_ingestion_usecase import BedrockIngestionUseCase
from src.shared.helpers.errors.usecase_errors import DataIngestionError

class Test_BedrockIngestionUseCase:
    @patch('src.modules.bedrock_ingestion.app.bedrock_ingestion_usecase.boto3')
    @patch('src.modules.bedrock_ingestion.app.bedrock_ingestion_usecase.os')
    def test_bedrock_ingestion_usecase(self, mock_os, mock_boto3):
        mock_os.environ.get.side_effect = lambda x: "mock_" + x.lower()
        mock_client = MagicMock()
        mock_boto3.client.return_value = mock_client
        mock_client.start_ingestion_job.return_value = {
            "ingestionJob": {
                "ingestionJobId": "mock_job_id",
                "status": "STARTING"
            }
        }
        
        usecase = BedrockIngestionUseCase()
        
        result = usecase("mock_bucket", "mock_object.pdf")
        
        assert result == {
            "job_id": "mock_job_id",
            "status": "STARTING"
        }
        mock_client.start_ingestion_job.assert_called_once_with(
            knowledgeBaseId="mock_knowledge_base_id",
            dataSourceId="mock_data_source_id",
            description="Auto-triggered by upload of mock_object.pdf from mock_bucket"
        )
        
    @patch('src.modules.bedrock_ingestion.app.bedrock_ingestion_usecase.boto3')
    @patch('src.modules.bedrock_ingestion.app.bedrock_ingestion_usecase.os')
    def test_bedrock_ingestion_usecase_error(self, mock_os, mock_boto3):
        mock_os.environ.get.side_effect = lambda x: "mock_" + x.lower()
        mock_client = MagicMock()
        mock_boto3.client.return_value = mock_client
        mock_client.start_ingestion_job.side_effect = Exception("AWS Error")
        
        usecase = BedrockIngestionUseCase()
        
        with pytest.raises(DataIngestionError) as exc_info:
            usecase("mock_bucket", "mock_object.pdf")
            
        assert str(exc_info.value) == "Error starting bedrock ingestion: AWS Error"
