import os
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_cognito,
    aws_iam
)
from constructs import Construct

from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")

        if 'prod' in self.github_ref_name: 
            self.dev_auth_system_userpool_arn = os.environ.get(
            "AUTH_DEV_SYSTEM_USERPOOL_ARN_PROD")

        else:
            self.dev_auth_system_userpool_arn = os.environ.get(
            "AUTH_DEV_SYSTEM_USERPOOL_ARN_DEV")
    
        self.aws_region = os.environ.get("AWS_REGION")
        
        self.rest_api = RestApi(self, "PortalInterno_RestApi",
                                rest_api_name="PortalInterno_RestApi",
                                description="This is the Portal Interno RestApi",
                                default_cors_preflight_options=
                                {
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
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
        
        ENVIRONMENT_VARIABLES = {
            "STAGE": self.github_ref_name.upper(),
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table_action.table_name,
            "DYNAMO_TABLE_NAME_MEMBER": self.dynamo_stack.dynamo_table_member.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
            "DYNAMO_GSI_PARTITION_KEY": "GSI1-PK",
            "DYNAMO_GSI_SORT_KEY": "GSI1-SK",
            "REGION": self.aws_region,
            "REPLY_TO_EMAIL": "dev@maua.br",
            "FROM_EMAIL": "contato@devmaua.com",
            "HIDDEN_COPY": "dev@maua.br",
            "S3_BUCKET_NAME_MEMBER": self.bucket_stack.s3_bucket_member.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS_MEMBER": self.bucket_stack.cloudfront_distribution_member.domain_name,
            "S3_BUCKET_NAME_PROJECT": self.bucket_stack.s3_bucket_project.bucket_name,
            "CLOUD_FRONT_DISTRIBUTION_DOMAIN_ASSETS_PROJECT": self.bucket_stack.cloudfront_distribution_project.domain_name,

        }
        
        self.cognito_auth = CognitoUserPoolsAuthorizer(self, f"port_cognito_auth_{self.github_ref_name}",
                                                       cognito_user_pools=[aws_cognito.UserPool.from_user_pool_arn(
                                                           self, f"port_cognito_auth_userpool_{self.github_ref_name}",
                                                           self.dev_auth_system_userpool_arn
                                                       )]
                                                       )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=self.cognito_auth)
        
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

        for f in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table_action.grant_read_write_data(f)
        
        for f in self.lambda_stack.functions_that_need_dynamo_member_permissions:
            self.dynamo_stack.dynamo_table_member.grant_read_write_data(f)
        
        for f in self.lambda_stack.functions_that_need_ses_permissions:
            f.add_to_role_policy(ses_admin_policy)

        for f in self.lambda_stack.functions_that_need_s3_permissions:
            f.add_to_role_policy(s3_admin_policy)
