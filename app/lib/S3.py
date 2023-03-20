import boto3
import requests
from collections import OrderedDict

class S3:
    def __init__(self, bucket: str) -> None:
        self.NONO_LIST = ["", "EXAMPLE"]
        self.ORDERING = ["comps", "latenite", "schmidtDecomp", "fireWalls", "qkd", "fractalsAndChaos"]

        self.bucket_name = bucket
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(bucket)
        self.client = boto3.client('s3')

    def list_projects(self) -> list:
        return list(set([obj.key.split('/')[1] for obj in self.bucket.objects.filter(Prefix="projects/") if obj.key.split('/')[1] not in self.NONO_LIST]))

    def get_url(self, project: str, key: str) -> str:
        print(f"https://ctbus-site-db.s3.amazonaws.com/projects/{project}/{key}")
        return f"https://ctbus-site-db.s3.amazonaws.com/projects/{project}/{key}"
    
    def project_dict(self, project_name: str) -> dict:
        d = {}

        if url := self.get_url(project_name, "thumbnail.png"):
            d["thumbnail"] = url
        if url := self.get_url(project_name, "title.txt"):
            response = requests.get(url)
            d["title"] = response.text
        if url := self.get_url(project_name, "description.txt"):
            response = requests.get(url)
            d["description"] = response.text
        if url := self.get_url(project_name, "tags.txt"):
            response = requests.get(url)
            d["tags"] = response.text
        if url := self.get_url(project_name, "body.pdf"):
            d["body"] = url
        if url := self.get_url(project_name, "slides.pptxs"):
            d["slides"] = url
        if url := self.get_url(project_name, "video.mp4"):
            d["video"] = url
        
        print(d)
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
