import boto3
from decouple import config


def upload_file(file_body, object_name=None):
    s3_client = boto3.client(
        config('SERVICE_NAME'),
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY')
    )

    s3_client.put_object(
        Body=file_body,
        Bucket=config('BUCKET_NAME'),
        Key=object_name,
    )


def get_file_content(file_name):
    s3 = boto3.resource(
        service_name=config('SERVICE_NAME'),
        aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY')
    )
    txt_file = s3.Object(config('BUCKET_NAME'), file_name).get()['Body'].read()

    return txt_file
   