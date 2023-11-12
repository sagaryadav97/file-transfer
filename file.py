import os
import boto3
from botocore.exceptions import NoCredentialsError

# Set your Linode Object Storage credentials
ACCESS_KEY = 'your_correct_access_key'
SECRET_KEY = 'your_correct_secret_key'
BUCKET_NAME = 'your_bucket_name'
ENDPOINT_URL = 'https://your-linode-endpoint.com'

# Function to download a folder and its contents
def download_folder(bucket, folder, local_path):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, endpoint_url=ENDPOINT_URL)

    # List objects in the folder
    objects = s3.list_objects_v2(Bucket=bucket, Prefix=folder).get('Contents', [])

    for obj in objects:
        # Get the key (object name)
        key = obj['Key']

        # Create local path for the file
        local_file_path = os.path.join(local_path, key)

        # Skip if the file already exists locally
        if os.path.exists(local_file_path):
            print(f"Skipped existing file: {key}")
            continue

        # Create local directory if it doesn't exist
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

        # Download the file
        s3.download_file(Bucket=bucket, Key=key, Filename=local_file_path)

        print(f"Downloaded file: {key}")

# Specify the folder you want to download
folder_to_download = 'wwf-images/complaint_attachments_vendor'

# Specify the local path to save the downloaded files
local_download_path = '/home/sagar/railfeast/filetransfer/'

# Download the folder and its contents
download_folder(BUCKET_NAME, folder_to_download, local_download_path)