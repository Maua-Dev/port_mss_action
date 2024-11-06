import os

from aws_cdk import (
    aws_s3, aws_s3_notifications, aws_lambda,
    aws_stepfunctions,
    aws_stepfunctions_tasks,
    aws_events, aws_events_targets,
    aws_cloudfront, aws_cloudfront_origins, RemovalPolicy
)

from constructs import Construct


class BucketStack(Construct):
    s3_bucket_member: aws_s3.Bucket
    s3_bucket_project: aws_s3.Bucket
    selfie_validation_step_function: aws_stepfunctions.StateMachine
    cloudfront_distribution_member: aws_cloudfront.Distribution
    cloudfront_distribution_project: aws_cloudfront.Distribution

    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "PortalInterno_Bucket")

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")

        REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref_name else RemovalPolicy.DESTROY

        self.s3_bucket_member = aws_s3.Bucket(self, "PortalInterno_Member_Photo_S3_Bucket",
                                       versioned=True,
                                       block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
                                       event_bridge_enabled=False,
                                       cors=[aws_s3.CorsRule(
                                             allowed_methods=[
                                                 aws_s3.HttpMethods.GET, aws_s3.HttpMethods.PUT, aws_s3.HttpMethods.POST],
                                             allowed_origins=["*"],
                                             allowed_headers=["*"],
                                             max_age=3000
                                             )],
                                       removal_policy=REMOVAL_POLICY
                                       )

        oai = aws_cloudfront.OriginAccessIdentity(self, "PortalInterno_Member_Photo_OAI",
                                                  comment="This is PortalInterno member photo OAI")
        
        self.s3_bucket_member.grant_read_write(oai)

        self.cloudfront_distribution_member = aws_cloudfront.Distribution(self, "PortalInterno_Member_Photo_CloudFront_Distribution",
                                                                     default_behavior=aws_cloudfront.BehaviorOptions(
                                                                          origin=aws_cloudfront_origins.S3Origin(
                                                                            self.s3_bucket_member,
                                                                            origin_access_identity=oai),
                                                                          origin_request_policy=aws_cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                                                                          viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                                                                          response_headers_policy=aws_cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                                                                          cache_policy=aws_cloudfront.CachePolicy.CACHING_OPTIMIZED,
                                                                          allowed_methods=aws_cloudfront.AllowedMethods.ALLOW_ALL
                                                                     )
                                                                     )
        
        self.s3_bucket_project = aws_s3.Bucket(self, "PortalInterno_Project_Photo_S3_Bucket",
                                versioned=True,
                                block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
                                event_bridge_enabled=False,
                                cors=[aws_s3.CorsRule(
                                        allowed_methods=[
                                            aws_s3.HttpMethods.GET, aws_s3.HttpMethods.PUT, aws_s3.HttpMethods.POST],
                                        allowed_origins=["*"],
                                        allowed_headers=["*"],
                                        max_age=3000
                                        )],
                                removal_policy=REMOVAL_POLICY
                                )

        oai = aws_cloudfront.OriginAccessIdentity(self, "PortalInterno_Project_Photo_OAI",
                                                  comment="This is PortalInterno project photo OAI")
        
        self.s3_bucket_project.grant_read_write(oai)

        self.cloudfront_distribution_project = aws_cloudfront.Distribution(self, "PortalInterno_Project_Photo_CloudFront_Distribution",
                                                                     default_behavior=aws_cloudfront.BehaviorOptions(
                                                                          origin=aws_cloudfront_origins.S3Origin(
                                                                            self.s3_bucket_project,
                                                                            origin_access_identity=oai),
                                                                          origin_request_policy=aws_cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                                                                          viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                                                                          response_headers_policy=aws_cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                                                                          cache_policy=aws_cloudfront.CachePolicy.CACHING_OPTIMIZED,
                                                                          allowed_methods=aws_cloudfront.AllowedMethods.ALLOW_ALL
                                                                     )
                                            )

