import json
import os
import boto3

def hello(event, context):

    ecr_repo = os.environ['ECR_REPO']
    ecr = boto3.client('ecr')
    s3 = boto3.client('s3')
    # change below to download_file
    s3_response = s3.get_response (
        Bucket = os.environ['DOCKERFILE_BUCKET'],
        Key = f'(os.environ['DEPLOY_ENV'])/Dockerfile' 
    )
    # dockerfile = 

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
