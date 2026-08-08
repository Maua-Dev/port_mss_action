import os
from constructs import Construct
from aws_cdk import (
    aws_s3vectors as s3vectors,
)


class VectorsBucketStack(Construct):
    def __init__(
        self,
        scope: Construct
    ) -> None:
        super().__init__(scope, "PortMssAction_VectorsBucket")

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME", "dev")

        stage= self.github_ref_name

        # cria o bucket de vetores
        self.s3_vectors_bucket_context_files= s3vectors.CfnVectorBucket(
            self,
            "PortalInterno_File_Vector_Bucket",
            vector_bucket_name=f"portal-interno-files-vector-{stage.lower()}",
        )

        self.s3_vectors_index= s3vectors.CfnIndex(
            self,
            "PortalInterno_File_Vector_Index",
            vector_bucket_name=self.s3_vectors_bucket_context_files.vector_bucket_name,
            index_name="portal-interno-index",
            dimension=1024,
            data_type="float32",
            distance_metric="cosine",
            metadata_configuration=s3vectors.CfnIndex.MetadataConfigurationProperty(
                non_filterable_metadata_keys=["AMAZON_BEDROCK_TEXT", "AMAZON_BEDROCK_METADATA"]
            )
        )

        # fala para o cloud formation para ele cria o bucket antes de criar o index
        self.s3_vectors_index.node.add_dependency(self.s3_vectors_bucket_context_files)

        self.vector_bucket_arn=self.s3_vectors_bucket_context_files.attr_vector_bucket_arn

        self.vector_index_arn=self.s3_vectors_index.attr_index_arn

    def grant_bedrock_access(self, role_arn: str) -> s3vectors.CfnVectorBucketPolicy:
        policy= s3vectors.CfnVectorBucketPolicy(
            self,
            "BedrockVectorBucketPolicy",
            vector_bucket_name=self.s3_vectors_bucket_context_files.vector_bucket_name,
            policy={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": role_arn
                        },
                        "Action": "s3vectors:*",
                        "Resource": "*"
                    }
                ]
            }
        )
        return policy