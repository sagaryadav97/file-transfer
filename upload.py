import os
import boto3
from botocore.exceptions import NoCredentialsError

# Set your AWS credentials and S3 bucket details
ACCESS_KEY = 'your_aws_access_key'
SECRET_KEY = 'your_aws_secret_key'
BUCKET_NAME = 'your_s3_bucket_name'
AWS_REGION = 'your_aws_region'


# Local folder path to upload
local_folder_path = '/home/sagar/railfeast/filetransfer/wwf-images'

# Target S3 folder (prefix)
s3_folder_prefix = 'wwf-images'


# Function to upload a local folder to S3
def upload_folder_to_s3(local_folder, bucket, s3_prefix=''):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name=AWS_REGION)

    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.join(s3_prefix, os.path.relpath(local_file_path, local_folder))

            # Upload the file to S3
            s3.upload_file(local_file_path, bucket, s3_key)

            print(f"Uploaded {local_file_path} to {s3_key}")

# Upload the entire local folder to S3
upload_folder_to_s3(local_folder_path, BUCKET_NAME, s3_folder_prefix)