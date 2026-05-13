
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration, CognitoUserPoolsAuthorizer
from aws_cdk.aws_events import Rule, Schedule
from aws_cdk.aws_events_targets import LambdaFunction

class LambdaStack(Construct):

    functions_that_need_dynamo_permissions = []
    functions_that_need_dynamo_member_permissions = []
    functions_that_need_dynamo_strike_permissions= []

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

    def create_lambda_event_bridge_integration(self,module_name: str,cron_schedule: Schedule.cron,environment_variables: dict = {"STAGE": "TEST"}):
        function = lambda_.Function(
            self,
            module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer, self.lambda_layer_pandas, self.lamba_layer_xlsxwriter],
            environment=environment_variables,
            timeout=Duration.seconds(15)
        )

        rule = Rule(
            self, f"{module_name.title()}EventRule",
            schedule=cron_schedule
        )

        rule.add_target(LambdaFunction(function))

        return function

    # this is an lambda that will not be acces by the internet through api gateway so it's only to be used by aws services
    def create_background_lambda(
        self,
        module_name: str,
        environment_variables: dict
    ):
        function= lambda_.Function(
            self,
            module_name.title(),
            function_name=f"portal-interno-{module_name}",
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            environment=environment_variables,
            timeout=Duration.seconds(35)
        )

        return function

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict,
                 authorizer: CognitoUserPoolsAuthorizer) -> None:
        super().__init__(scope, "PortalInterno_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "PortalInterno_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )

        self.lambda_layer_pandas = lambda_.LayerVersion(self, "PortalInterno_Layer_Pandas",
                                                        code=lambda_.Code.from_asset("./lambda_requirements_layer_temp/pandas"),
                                                        compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                        )

        self.lamba_layer_xlsxwriter = lambda_.LayerVersion(self, "PortalInterno_Layer_XlsxWriter",
                                                              code=lambda_.Code.from_asset("./lambda_requirements_layer_temp/xlsxwriter"),
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

        self.create_strike_function= self.create_lambda_api_gateway_integration(
            module_name="create_strike",
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

        self.delete_strike_function= self.create_lambda_api_gateway_integration(
            module_name="delete_strike",
            method="DELETE",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_strike_function= self.create_lambda_api_gateway_integration(
            module_name="get_strike",
            method="GET",
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

        self.get_history_project_function = self.create_lambda_api_gateway_integration(
            module_name="get_history_project",
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

        self.get_member_info_function = self.create_lambda_api_gateway_integration(
            module_name="get_member_info",
            method="GET",
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

        self.download_members_function = self.create_lambda_event_bridge_integration(
            module_name="download_members",
            cron_schedule=Schedule.cron(week_day="TUE", hour="18", minute="0"),
            environment_variables=environment_variables
        )

        self.download_actions_function = self.create_lambda_event_bridge_integration(
            module_name="download_actions",
            cron_schedule=Schedule.cron(week_day="TUE", hour="18", minute="0"),
            environment_variables=environment_variables
        )

        self.download_projects_function = self.create_lambda_api_gateway_integration(
            module_name="download_projects",
            method="PUT",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_upload_url = self.create_lambda_api_gateway_integration(
            module_name="get_upload_url",
            method="PUT",
            api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        
        self.bedrock_ingestion= self.create_background_lambda(
            module_name="bedrock_ingestion",
            environment_variables=environment_variables
        )


        self.functions_that_need_dynamo_strike_permissions = [
            self.create_strike_function,
            self.delete_strike_function,
            self.get_all_members_admin_function,
            self.get_all_members_function,
            self.get_member_function,
            self.get_strike_function
        ]

        self.functions_that_need_dynamo_permissions = [
                self.create_action_function,
                self.create_project_function,
                self.create_member_function,
                self.create_strike_function,
                self.delete_project_function,
                self.delete_member_function,
                self.get_all_projects_function,
                self.batch_get_member_function,
                self.get_history_function,
                self.get_history_project_function,
                self.get_member_function,
                self.get_member_info_function,
                self.get_project_function,
                self.get_all_members_function,
                self.get_all_members_admin_function,
                self.update_project_function,
                self.update_action_function,
                self.update_action_validation_function,
                self.update_member_function,
                self.delete_action_function,
                self.download_projects_function,
                self.download_members_function,
                self.download_actions_function,
        ]

        self.functions_that_need_dynamo_member_permissions = [
                self.create_action_function,
                self.create_project_function,
                self.create_member_function,
                self.create_strike_function,
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
                self.get_member_info_function,
                self.get_all_projects_function,
                self.get_history_function,
                self.get_history_project_function,
                self.get_project_function,
                self.delete_action_function,
                self.delete_strike_function,
                self.download_projects_function,
                self.download_members_function,
                self.download_actions_function,
                self.get_strike_function
        ]

        self.functions_that_need_ses_permissions = [
            self.update_member_function,
            self.update_action_validation_function,
            self.download_projects_function,
            self.download_members_function,
            self.download_actions_function,
            self.create_strike_function
        ]

        self.functions_that_need_s3_permissions = [
            self.create_member_function,
            self.update_member_function,
            self.create_project_function,
            self.update_project_function,
            self.download_projects_function,
            self.download_members_function
        ]

        self.functions_that_need_bedrock_access= [
            self.bedrock_ingestion
        ]

