import os 


from aws_cdk import (
    CfnOutput,
    aws_dynamodb,
    RemovalPolicy
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration

class DynamoStack(Construct):

        def __init__(self, scope: Construct) -> None:
                super().__init__(scope, "PortalInterno_Dynamo")

                self.github_ref_name = os.environ.get("GITHUB_REF_NAME")

                REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref_name else RemovalPolicy.DESTROY

                self.dynamo_table_action = aws_dynamodb.Table(
                self, "PortalInterno_action_Table",
                partition_key=aws_dynamodb.Attribute(
                    name="PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                point_in_time_recovery=True,
                sort_key=aws_dynamodb.Attribute(
                    name="SK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
                removal_policy=REMOVAL_POLICY
            )
                
                self.dynamo_table_action.add_global_secondary_index(
                partition_key=aws_dynamodb.Attribute(
                    name="GSI1-PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                sort_key=aws_dynamodb.Attribute(
                    name="GSI1-SK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                index_name="GSI1"
            )
                
                self.dynamo_table_action.add_local_secondary_index(
                    index_name="LSI1",
                    sort_key=aws_dynamodb.Attribute(
                        name="start_date",
                        type=aws_dynamodb.AttributeType.NUMBER
                    ),
                    
                )
            
                self.dynamo_table_member = aws_dynamodb.Table(
                self, "PortalInterno_member_Table",
                partition_key=aws_dynamodb.Attribute(
                    name="PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                point_in_time_recovery=True,
                sort_key=aws_dynamodb.Attribute(
                    name="SK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
                removal_policy=REMOVAL_POLICY
            )    
                CfnOutput(self, 'DynamoActionRemovalPolicy',
                    value=REMOVAL_POLICY.value,
                    export_name=f'PortalInterno{self.github_ref_name}DynamoActionRemovalPolicyValue')
                
                CfnOutput(self, 'DynamoMemberRemovalPolicy',
                    value=REMOVAL_POLICY.value,
                    export_name=f'PortalInterno{self.github_ref_name}DynamoMemberRemovalPolicyValue') 
            