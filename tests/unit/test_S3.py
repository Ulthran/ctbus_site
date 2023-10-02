import os
import pytest
from app.S3 import S3
from botocore.exceptions import ClientError


class MockS3Client:
    def __init__(self, bucket_name: str, FNE: bool = False):
        self.bucket_name = bucket_name
        self.FNE = FNE

    def download_file(self, bucket_name: str, key: str, filename: str):
        if self.FNE:
            raise ClientError

        result = {"VAR1": "value1"}

        with open(".env", "w") as f:
            for k, v in result.items():
                f.write(f"{k}={v}\n")


@pytest.fixture
def s3_setup():
    bucket_name = "test-bucket"
    s3 = S3(bucket_name, MockS3Client(bucket_name))

    yield s3

    os.remove(".env")


def test_get_env_file_exists(s3_setup):
    s3 = s3_setup
    result = {"VAR1": "value1", "VAR2": "value2"}

    with open(".env", "w") as f:
        for k, v in result.items():
            f.write(f"{k}={v}\n")

    # Assert that the expected result is returned
    assert s3.get_env() == {"VAR1": "value1", "VAR2": "value2"}


def test_get_env_file_does_not_exist(s3_setup):
    s3 = s3_setup

    # Assert that the expected result is returned
    assert s3.get_env() == {"VAR1": "value1"}
