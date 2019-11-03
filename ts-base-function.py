import json

# lambda_handler is the intial point of execution for this Lambda function
# Event from the handler contains JSON data recieved through the API Gateway
def lambda_handler(event, context):
    print(event)
    return "Hello"