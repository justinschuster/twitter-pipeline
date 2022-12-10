import boto3
import json
import os

import config

aws_access_key = config.AWS_ACCESS_KEY
aws_secret_key= config.AWS_SECRET_KEY

s3_bucket = 's3-bucket-language-meter'
json_path = 'language-meter/json'

def init_s3_client():
    """
    Establishes S3 client using boto3.

    Returns boto3 client object
    """
    s3_client = boto3.client(   's3',
                                aws_access_key_id=aws_access_key,
                                aws_secret_access_key=aws_secret_key
    )
    return s3_client

def upload_to_s3(json_path, json_data, csv_path, csv_buffer) -> None:
    s3 = init_s3_client()
    s3.put_object(Body=json.dumps(json_data), Bucket=s3_bucket, Key=json_path, ContentType='application/json')
    s3.put_object(Body=csv_buffer.getvalue(), Bucket=s3_bucket, Key=csv_path)

def print_file_names():
    json_path = 'language-meter/json'
    files = os.listdir(json_path)
    files = [f for f in files if os.path.isfile('{}/{}'.format(json_path, f))]
    print(*files, sep='\n')
