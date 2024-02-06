import aws_cdk as core
import aws_cdk.assertions as assertions

from first_cdk1.first_cdk1_stack import FirstCdk1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in first_cdk1/first_cdk1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FirstCdk1Stack(app, "first-cdk1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
