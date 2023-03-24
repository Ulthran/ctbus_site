import boto3
import requests
from collections import OrderedDict
from app.Backend import Backend

class S3(Backend):
    def __init__(self, bucket: str) -> None:
        super().__init__()
        self.NONO_LIST = ["", "EXAMPLE"]
        self.ORDERING = ["comps", "latenite", "schmidtDecomp", "fireWalls", "qkd", "fractalsAndChaos"]

        self.bucket_name = bucket
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(bucket)
        self.client = boto3.client('s3')

    def list_projects(self) -> list:
        return list(set([obj.key.split('/')[1] for obj in self.bucket.objects.filter(Prefix="projects/") if obj.key.split('/')[1] not in self.NONO_LIST]))
    
    def project_dict(self, project_name: str) -> dict:
        d = super().project_dict(project_name)

        if url := self.get_url(project_name, "title.txt"):
            response = requests.get(url)
            d["title"] = response.text
        if url := self.get_url(project_name, "description.txt"):
            response = requests.get(url)
            d["description"] = response.text
        if url := self.get_url(project_name, "tags.txt"):
            response = requests.get(url)
            d["tags"] = response.text
        
        return d
        
    def projects_dict(self) -> dict:
        d = OrderedDict()

        for project in self.list_projects():
            e = {}

            if url := self.get_url(project, "thumbnail.png"):
                e["thumbnail"] = url
            if url := self.get_url(project, "title.txt"):
                response = requests.get(url)
                e["title"] = response.text
            if url := self.get_url(project, "description.txt"):
                response = requests.get(url)
                e["description"] = response.text
            if url := self.get_url(project, "tags.txt"):
                response = requests.get(url)
                e["tags"] = response.text

            d[project] = e
        
        return d
