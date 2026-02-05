import json
import boto3

lambda_client = boto3.client('lambda')


def lambda_handler(event, context):
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    return response
