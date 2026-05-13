import os
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_iam,
    aws_events_targets as targets
) 
from constructs import Construct

from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack
from .cognito_stack import CognitoStack
from .event_bridge_stack import EventBridgeStack
from .vectors_bucket_stack import VectorsBucketStack
from .bedrock_stack import BedrockStack

from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        
        self.rest_api = RestApi(
            self, "PortalInterno_RestApi",
            rest_api_name="PortalInterno_RestApi",
            description="This is the Portal Interno RestApi",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["*"]
            },
            deploy_options={
                "stage_name": self.github_ref_name.lower()
            }
        )

        api_gateway_resource = self.rest_api.root.add_resource("mss-action", default_cors_preflight_options=
        {
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
                                                                   )
        
        self.dynamo_stack = DynamoStack(self)

        self.bucket_stack = BucketStack(self)

        # Create Cognito stack
        self.cognito_stack = CognitoStack(self, "CognitoStack", stage=self.github_ref_name)
        
        ENVIRONMENT_VARIABLES = {
            "STAGE": self.github_ref_name.upper(),
            "DYNAMO_TABLE_NAME_STRIKE": self.dynamo_stack.dynamo_table_strike.table_name,
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table_action.table_name,
            "DYNAMO_TABLE_NAME_MEMBER": self.dynamo_stack.dynamo_table_member.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
            "DYNAMO_GSI_PARTITION_KEY": "GSI1-PK",
            "DYNAMO_GSI_SORT_KEY": "GSI1-SK",
            "DYNAMO_GSI_TARGET_PARTITION_KEY": "GSI-TARGET-PK",
            "DYNAMO_GSI_TARGET_SORT_KEY": "GSI-TARGET-SK",
            "REGION": self.aws_region,
            "REPLY_TO_EMAIL": os.environ.get("REPLY_TO_EMAIL", "dev@maua.br"),
            "FROM_EMAIL": os.environ.get("FROM_EMAIL", "contato@devmaua.com"),
            "HIDDEN_COPY": os.environ.get("HIDDEN_COPY", "dev@maua.br"),
            "S3_BUCKET_NAME_MEMBER": self.bucket_stack.s3_bucket_member.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS_MEMBER": self.bucket_stack.cloudfront_distribution_member.domain_name,
            "S3_BUCKET_NAME_PROJECT": self.bucket_stack.s3_bucket_project.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS_PROJECT": self.bucket_stack.cloudfront_distribution_project.domain_name,
            "S3_BUCKET_NAME_MEMBER_REPORT": self.bucket_stack.s3_bucket_member_report.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS_MEMBER_REPORT": self.bucket_stack.cloudfront_distribution_member_report.domain_name,
            "S3_BUCKET_NAME_DEV_POLICY_DOCUMENTS": self.bucket_stack.s3_bucket_dev_policy_documents.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS_DEV_POLICY_DOCUMENTS": self.bucket_stack.cloudfront_distribution_dev_policy_documents.domain_name,
            "COGNITO_USER_POOL_ID": self.cognito_stack.user_pool.user_pool_id,
            "COGNITO_CLIENT_ID": self.cognito_stack.client.user_pool_client_id,
            "MSS_NAME": os.environ.get("MSS_NAME", "port_mss_action"),
            "S3_ASSETS_CDN": os.environ.get("S3_ASSETS_CDN", ""),

        }
        
        # Use the new Cognito stack for authorization
        self.cognito_auth = CognitoUserPoolsAuthorizer(self, f"port_cognito_auth_{self.github_ref_name}",
                                                       cognito_user_pools=[self.cognito_stack.user_pool]
                                                       )

        self.s3_vectors_bucket_stack= VectorsBucketStack(self)


        self.bedrock_stack= BedrockStack(
            self,
            vector_bucket_arn=self.s3_vectors_bucket_stack.vector_bucket_arn,
            vector_index_arn=self.s3_vectors_bucket_stack.vector_index_arn,
            bucket_arn=self.bucket_stack.s3_bucket_dev_policy_documents.bucket_arn
        )

        self.event_bridge_stack= EventBridgeStack(self, self.bucket_stack.s3_bucket_dev_policy_documents.bucket_name)

        # permitindo que a kb_role do bedrock leia arquivos do s3
        self.bucket_stack.s3_bucket_dev_policy_documents.grant_read(self.bedrock_stack.kb_role)


        # permitindo que a role assumida pelo bedrock tenha acesso ao s3 vectors
        vector_bucket_policy=self.s3_vectors_bucket_stack.grant_bedrock_access(role_arn=self.bedrock_stack.kb_role.role_arn)

        # fazendo o bedrock esperar pela policy ser criada e atrelada a ele
        self.bedrock_stack.knowledge_base.node.add_dependency(vector_bucket_policy)


        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=self.cognito_auth)


        # add the lambda to be trigged by the event bridge when the .pdf object is added/removed to s3
        self.event_bridge_stack.trigger_ingestion_rule.add_target(
            targets.LambdaFunction(
                handler=self.lambda_stack.bedrock_ingestion
            )
        )
        
        ses_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "ses:*",
            ],
            resources=[
                "*"
            ]
        )

        s3_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "s3:*",
            ],
            resources=[
                "*"
            ]
        )

        for f in self.lambda_stack.functions_that_need_dynamo_strike_permissions:
            self.dynamo_stack.dynamo_table_strike.grant_read_write_data(f)

        for f in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table_action.grant_read_write_data(f)
        
        for f in self.lambda_stack.functions_that_need_dynamo_member_permissions:
            self.dynamo_stack.dynamo_table_member.grant_read_write_data(f)
        
        for f in self.lambda_stack.functions_that_need_ses_permissions:
            f.add_to_role_policy(ses_admin_policy)

        for f in self.lambda_stack.functions_that_need_s3_permissions:
            f.add_to_role_policy(s3_admin_policy)

        # bedrock access
        bedrock_policy= aws_iam.PolicyStatement(
            actions=[
                "bedrock:RetrieveAndGenerate",
                "bedrock:Retrieve",
                "bedrock:StartIngestionJob"
            ],
            resources=[
                # this one gives acces to the Kb it self
                self.bedrock_stack.knowledge_base.attr_knowledge_base_arn,
                
                # this line line below it gives access to the datasource and Jobs inside KB
                f"{self.bedrock_stack.knowledge_base.attr_knowledge_base_arn}/*"
            ]
        )

        for fn in self.lambda_stack.functions_that_need_bedrock_access:
            fn.add_to_role_policy(bedrock_policy)

        