import boto3
from src.shared.environments import Environments


class S3Manager:

    def __init__(self):
        self.__envs = Environments.get_envs()
        stage = self.__envs.stage.value
        if stage == "TEST":
            self.s3 = boto3.client(
                "s3",
                aws_access_key_id=self.__envs.client_id,
                endpoint_url=self.__envs.bucket_endpoint_url,
                region_name=self.__envs.region,
                config=boto3.session.Config(signature_version="s3v4")
            )
        else:
            self.s3 = boto3.client("s3")

    def upload_file(self, key, file_type, decode_string):

        response = self.s3.put_object(
            Bucket = self.__envs.s3_bucket_name,
            Key = key,
            Body = decode_string,
            ContentType = file_type.replace(".",""),
        )

        return {
            's3_response': response,
            'key': key
        }
    
    