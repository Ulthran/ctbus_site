import boto3
import os
from botocore.exceptions import ClientError


class S3:
    def __init__(self, bucket: str, client=None):
        self.bucket_name = bucket
        if client:
            self.client = client
        else:
            self.client = boto3.client("s3")

    def get_env(self) -> dict:
        if not os.path.exists(".env"):
            try:
                self.client.download_file(self.bucket_name, ".env", ".env")
            except ClientError:
                pass

        with open(".env", "r") as f:
            return {
                line.split("=")[0]: line.split("=")[1].strip()
                for line in f.readlines()
                if line.strip()
            }
