from src.modules.bedrock_ingestion.app.bedrock_ingestion_viewmodel import BedrockIngestionViewModel

class Test_BedrockIngestionViewModel:
    def test_bedrock_ingestion_viewmodel(self):
        data = {
            "job_id": "test_job_id",
            "status": "STARTING"
        }
        
        viewmodel = BedrockIngestionViewModel(data)
        
        response = viewmodel.to_dict()
        
        assert response == {
            'data': data,
            'message': 'Bedrock ingestion started successfully'
        }
