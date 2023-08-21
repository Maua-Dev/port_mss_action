
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class LambdaStack(Construct):

    functions_that_need_dynamo_permissions = []

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, mss_action_api_resource: Resource, environment_variables: dict = {"STAGE": "TEST"}):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            environment=environment_variables,
            timeout=Duration.seconds(15)
        )

        mss_action_api_resource.add_resource(module_name.replace("_", "-")).add_method(method,
                                                                                        integration=LambdaIntegration(
                                                                                            function))

        return function

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict) -> None:
        super().__init__(scope, "PortalInterno_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "PortalInterno_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )
        
        self.create_action_function = self.create_lambda_api_gateway_integration(
            module_name="create_action",
            method="POST",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.create_project_function = self.create_lambda_api_gateway_integration(
            module_name="create_project",
            method="POST",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.delete_project_function = self.create_lambda_api_gateway_integration(
            module_name="delete_project",
            method="DELETE",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        self.get_all_projects_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_projects",
            method="GET",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.get_history_function = self.create_lambda_api_gateway_integration(
            module_name="get_history",
            method="GET",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.get_member_function = self.create_lambda_api_gateway_integration(
            module_name="get_member",
            method="GET",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.get_project_function = self.create_lambda_api_gateway_integration(
            module_name="get_project",
            method="GET",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.get_all_members_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_members",
            method="GET",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.update_project_function = self.create_lambda_api_gateway_integration(
            module_name="update_project",
            method="PUT",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )
        
        self.update_action_function = self.create_lambda_api_gateway_integration(
            module_name="update_action",
            method="PUT",
            mss_action_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )