from src.shared.environments import STAGE
import boto3
from src.shared.environments import Environments


class S3Manager:

    def __init__(self):
        self.__envs = Environments.get_envs()

        # Conecta ao MinIO se estiver rodando no estagio de test
        if self.__envs.stage == STAGE.TEST:
            self.s3 = boto3.client(
                "s3",
                endpoint_url=self.__envs.bucket_endpoint_url, # Aponta para a mesma porta do MinIo
                aws_access_key_id="root",
                aws_secret_access_key="root1234",
                region_name="sa-east-1"
            )
        else:
            self.s3 = boto3.client("s3")

    def upload_file(self, key, file_type, decode_string):

        response = self.s3.put_object(
            Bucket = self.__envs.s3_bucket_name_member_report,
            Key = key,
            Body = decode_string,
            ContentType = file_type.replace(".",""),
        )

        return {
            's3_response': response,
            'key': key
        }

    def generate_presigned_url(self, key: str, expiration: int = 3600) -> str:
        url = self.s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': self.__envs.s3_bucket_name_dev_policy_documents,
                'Key': key,
                'ContentType': 'application/pdf',
            },
            ExpiresIn=expiration
        )
        return url

