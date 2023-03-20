import boto3

class S3:
    def __init__(self, bucket: str) -> None:
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(bucket)

    def list_projects(self) -> list:
        return [obj for obj in self.bucket.objects.filter(Prefix="projects/")]
