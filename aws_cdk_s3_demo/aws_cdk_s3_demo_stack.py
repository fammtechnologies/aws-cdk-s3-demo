from aws_cdk import (
    Stack,
    aws_s3 as s3,
)

from constructs import Construct


class AwsCdkS3DemoStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:

        super().__init__(scope, construct_id, **kwargs)

        # Create S3 Bucket
        bucket = s3.Bucket(
            self,
            "DemoS3Bucket0107",
        )
