import os
from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    CfnOutput,
    aws_cognito as cognito,
    aws_lambda as _lambda,
)

class CognitoStack(Construct):
    def __init__(self, scope: Construct, construct_id: str, *, stage: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        github_ref = os.environ.get("GITHUB_REF_NAME", stage)

        # self.custom_message_fn = _lambda.Function(
        #     self, f"CustomMessageFn-{stage}",
        #     runtime=_lambda.Runtime.PYTHON_3_9,
        #     handler="handler.handler",
        #     code=_lambda.Code.from_asset("src/cognito_triggers/custom_message"),
        #     timeout=Duration.seconds(10),
        #     memory_size=256,
        #     environment={
        #         "STAGE": stage,
        #         "CONFIRMATION_URL_BASE": os.environ.get(
        #             "CONFIRMATION_URL_BASE",
        #             "https://portal-interno.dev/auth/confirm" 
        #         )
        #     }
        # )

        self.user_pool = cognito.UserPool(
            self, f"PortalInternoUserPool-{stage}",
            self_sign_up_enabled=True,
            sign_in_aliases=cognito.SignInAliases(email=True),
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(required=True, mutable=False),
                preferred_username=cognito.StandardAttribute(required=False, mutable=True),
            ),
            auto_verify=cognito.AutoVerifiedAttrs(email=True),
            account_recovery=cognito.AccountRecovery.EMAIL_ONLY,
            password_policy=cognito.PasswordPolicy(
                min_length=8,
                require_lowercase=True,
                require_uppercase=True,
                require_digits=True,
                require_symbols=False,
                temp_password_validity=Duration.days(7)
            ),
            removal_policy=RemovalPolicy.DESTROY  #todo mudar para RETAIN em produção
        )

        self.client = self.user_pool.add_client(
            f"PortalInternoUserPoolClient-{stage}",
            auth_flows=cognito.AuthFlow(
                user_srp=True,
                user_password=True,
                admin_user_password=True
            ),
            generate_secret=False,
            prevent_user_existence_errors=True,
            access_token_validity=Duration.hours(1),
            id_token_validity=Duration.hours(1),
            refresh_token_validity=Duration.days(30),
        )


        CfnOutput(self, f"UserPoolId-{stage}", value=self.user_pool.user_pool_id)
        CfnOutput(self, f"UserPoolClientId-{stage}", value=self.client.user_pool_client_id)
        CfnOutput(self, f"UserPoolArn-{stage}", value=self.user_pool.user_pool_arn)
