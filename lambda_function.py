#testing lambda function
import application


def lambda_handler(event, context):
    return application.greeting
