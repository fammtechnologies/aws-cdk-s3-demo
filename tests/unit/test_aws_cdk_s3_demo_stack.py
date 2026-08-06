import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_s3_demo.aws_cdk_s3_demo_stack import AwsCdkS3DemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_s3_demo/aws_cdk_s3_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkS3DemoStack(app, "aws-cdk-s3-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
