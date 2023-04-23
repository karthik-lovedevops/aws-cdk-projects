from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


class CdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime = _lambda.Runtime.PYTHON_3_9,
            code = _lambda.Code.from_asset('lambda'),
            handler='hello.handler'
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )

        

        # queue = sqs.Queue(
        #     self, "CdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #     self, "CdkProjectTopic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))
