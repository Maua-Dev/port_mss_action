import boto3
import os
from src.shared.helpers.errors.usecase_errors import DataIngestionError

class BedrockIngestionUseCase:
    def __init__(self):
        self.client= boto3.client('bedrock-agent')
        self.knowledge_base_id= os.environ.get("KNOWLEDGE_BASE_ID")
        self.data_source_id= os.environ.get("DATA_SOURCE_ID")

    def __call__(
        self,
        bucket_name: str,
        object_key: str
    ): 
        try:
            response= self.client.start_ingestion_job(
                knowledgeBaseId=self.knowledge_base_id,
                dataSourceId=self.data_source_id,
                description=f"Auto-triggered by upload of {object_key} from {bucket_name}"
            )

            return {
                "job_id": response["ingestionJob"]["ingestionJobId"],
                "status": response['ingestionJob']['status']
            }

        except Exception as e:
            raise DataIngestionError(str(e))
