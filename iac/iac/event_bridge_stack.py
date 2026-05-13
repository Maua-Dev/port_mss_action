import os
from constructs import Construct
from aws_cdk import (
    aws_events as events
)

class EventBridgeStack(Construct):
    def __init__(
        self,
        scope: Construct,
        s3_bucket_name: str
    ) -> None:
        super().__init__(scope, "PortMssAction_EventBridge")

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME", "dev")

        stage = self.github_ref_name

        self.trigger_ingestion_rule= events.Rule(
            self,
            "PDFUploadIngestionRule",
            rule_name=f"trigger-bedrock-ingestion-{stage.lower()}",
            description="Triggers the Bedrock KB sync when a new PDF is uploaded.",
            event_pattern=events.EventPattern(
                source=["aws.s3"],
                detail_type=[
                    "Object Created",
                    "Object Deleted"
                ],
                detail={
                    "bucket": {
                        "name": [s3_bucket_name]
                    },
                    "object": {
                        "key": [{"suffix": ".pdf"}]
                    }
                }
            )
        )