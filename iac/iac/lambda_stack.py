
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration, CognitoUserPoolsAuthorizer


class LambdaStack(Construct):

    functions_that_need_dynamo_permissions = []
    functions_that_need_dynamo_member_permissions = []

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, api_resource: Resource, environment_variables: dict = {"STAGE": "TEST"}, authorizer=None ):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            environment=environment_variables,
            timeout=Duration.seconds(15)
        )

        api_resource.add_resource(module_name.replace("_", "-")).add_method(method,
                                                                                        integration=LambdaIntegration(
                                                                                            function),
                                                                                        authorizer=authorizer)

        return function

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict,
                 authorizer: CognitoUserPoolsAuthorizer) -> None:
        super().__init__(scope, "PortalInterno_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "PortalInterno_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )
                
        self.create_action_function = self.create_lambda_api_gateway_integration(
            module_name="create_action",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.create_project_function = self.create_lambda_api_gateway_integration(
            module_name="create_project",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.create_member_function = self.create_lambda_api_gateway_integration(
            module_name="create_member",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.delete_project_function = self.create_lambda_api_gateway_integration(
            module_name="delete_project",
            method="DELETE",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.delete_member_function = self.create_lambda_api_gateway_integration(
            module_name="delete_member",
            method="DELETE",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_all_projects_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_projects",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.get_history_function = self.create_lambda_api_gateway_integration(
            module_name="get_history",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.get_member_function = self.create_lambda_api_gateway_integration(
            module_name="get_member",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.get_project_function = self.create_lambda_api_gateway_integration(
            module_name="get_project",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.get_all_members_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_members",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_all_members_admin_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_members_admin",
            method="POST",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.update_project_function = self.create_lambda_api_gateway_integration(
            module_name="update_project",
            method="PUT",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.update_member_function = self.create_lambda_api_gateway_integration(
            module_name="update_member",
            method="PUT",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.update_action_function = self.create_lambda_api_gateway_integration(
            module_name="update_action",
            method="PUT",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.batch_get_member_function = self.create_lambda_api_gateway_integration(
            module_name="batch_get_member",
            method="GET",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.update_action_validation_function = self.create_lambda_api_gateway_integration(
            module_name="update_action_validation",
            method="PUT",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.delete_action_function = self.create_lambda_api_gateway_integration(
            module_name="delete_action",
            method="DELETE",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.functions_that_need_dynamo_permissions = [
                self.create_action_function,
                self.create_project_function,
                self.create_member_function,
                self.delete_project_function,
                self.delete_member_function,
                self.get_all_projects_function,
                self.batch_get_member_function,
                self.get_history_function,
                self.get_member_function,
                self.get_project_function,
                self.get_all_members_function,
                self.get_all_members_admin_function,
                self.update_project_function,
                self.update_action_function,
                self.update_action_validation_function,
                self.update_member_function,
                self.delete_action_function
        ]
        
        self.functions_that_need_dynamo_member_permissions = [
                self.create_action_function,
                self.create_project_function,
                self.create_member_function,
                self.delete_member_function,
                self.delete_project_function,
                self.update_member_function,
                self.update_project_function,
                self.update_action_function,
                self.update_action_validation_function,
                self.get_all_members_function,
                self.get_all_members_admin_function,
                self.batch_get_member_function,
                self.get_member_function,
                self.get_all_projects_function,
                self.get_history_function,
                self.get_project_function,
                self.delete_action_function
        ]
        
        self.functions_that_need_ses_permissions = [
            self.update_member_function,
            self.update_action_validation_function
        ]

        self.functions_that_need_s3_permissions = [
            self.create_member_function,
            self.update_member_function,
            self.create_project_function,
            self.update_project_function,
        ]

        
