import os
from constructs import Construct
from aws_cdk import (
    aws_iam as iam,
    aws_bedrock as bedrock,
    aws_s3 as s3,
)

class BedrockStack(Construct):
    def __init__(
        self,
        scope: Construct,
        vector_bucket_arn: str,
        vector_index_arn: str,
        bucket_arn: str,
    ) -> None:
        super().__init__(scope, "PortMssAction_Bedrock")

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME", "dev")
        
        stage= self.github_ref_name

        self.kb_role= iam.Role(
            self,
            "BedrocKnowledgeBaseRole",
            role_name=f"BedrockKBRole-{stage}",
            assumed_by=iam.ServicePrincipal("bedrock.amazonaws.com"),
        )


        kb_setup_policy= iam.Policy(
            self,
            "BedrockKBSetupPolicy",
            statements=[
                iam.PolicyStatement(
                    actions=["bedrock:InvokeModel"],
                    resources=[f"arn:aws:bedrock:{os.environ.get('REGION', 'us-east-1')}::foundation-model/amazon.titan-embed-text-v2:0"]
                ),
                iam.PolicyStatement(
                    actions=[
                        "s3vectors:PutVectors",
                        "s3vectors:QueryVectors",
                        "s3vectors:GetVectors",
                        "s3vectors:DeleteVectors",
                        "s3vectors:GetIndex", 
                        "s3vectors:GetVectorBucket" 
                    ],
                    resources=[
                        vector_bucket_arn, 
                        vector_index_arn,
                        f"{vector_bucket_arn}/*",
                        f"{vector_index_arn}/*"
                    ]
                )

            ]
        )

        # Adiciona as permissoes a minha role
        self.kb_role.attach_inline_policy(kb_setup_policy)

        self.knowledge_base= bedrock.CfnKnowledgeBase(
            self,
            "PortMssAction_KnowledgeBase",
            name=f"port-mss-action-kb-{stage.lower()}",
            role_arn=self.kb_role.role_arn,
            knowledge_base_configuration=bedrock.CfnKnowledgeBase.KnowledgeBaseConfigurationProperty(
                type="VECTOR",
                vector_knowledge_base_configuration=bedrock.CfnKnowledgeBase.VectorKnowledgeBaseConfigurationProperty(
                    embedding_model_arn=f"arn:aws:bedrock:{os.environ.get('REGION', 'us-east-1')}::foundation-model/amazon.titan-embed-text-v2:0",
                    embedding_model_configuration=bedrock.CfnKnowledgeBase.EmbeddingModelConfigurationProperty(
                        bedrock_embedding_model_configuration=bedrock.CfnKnowledgeBase.BedrockEmbeddingModelConfigurationProperty(
                            dimensions=1024
                        )
                    )
                )
            ),
            storage_configuration= bedrock.CfnKnowledgeBase.StorageConfigurationProperty(
                type="S3_VECTORS",
                s3_vectors_configuration=bedrock.CfnKnowledgeBase.S3VectorsConfigurationProperty(
                    vector_bucket_arn=vector_bucket_arn,
                    index_arn=vector_index_arn
                )
            )
        )

        # forca o kb esperar as permissoes serem atreladas a ele
        self.knowledge_base.node.add_dependency(kb_setup_policy)

        self.data_source= bedrock.CfnDataSource(
            self,
            "PortMssAction_DataSource",
            knowledge_base_id=self.knowledge_base.attr_knowledge_base_id,
            name=f"S3_Context_Files_{stage}",
            data_source_configuration=bedrock.CfnDataSource.DataSourceConfigurationProperty(
                type="S3",
                s3_configuration=bedrock.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_arn=bucket_arn
                )
            ),
            vector_ingestion_configuration=bedrock.CfnDataSource.VectorIngestionConfigurationProperty(
                chunking_configuration=bedrock.CfnDataSource.ChunkingConfigurationProperty(
                    chunking_strategy="SEMANTIC",
                    semantic_chunking_configuration=bedrock.CfnDataSource.SemanticChunkingConfigurationProperty(
                        breakpoint_percentile_threshold=95,
                        buffer_size=1,
                        max_tokens=800
                    )
                )   
            )
        )