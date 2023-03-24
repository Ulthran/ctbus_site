import boto3
import requests

class DB:
    def __init__(self) -> None:
        pass

    def list_projects(self) -> list:
        raise NotImplementedError

    def url_exists(self, url):
        request = requests.head(url)
        if request.status_code == 200:
            return True
        else:
            return False

    def get_url(self, project: str, key: str) -> str:
        url = f"https://ctbus-site-db.s3.amazonaws.com/projects/{project}/{key}"
        print(url)
        if self.url_exists(url):
            return url
    
    def project_dict(self, project_name: str) -> dict:
        d = {}

        if url := self.get_url(project_name, "thumbnail.png"):
            d["thumbnail"] = url
        if url := self.get_url(project_name, "body.pdf"):
            d["body"] = url
        if url := self.get_url(project_name, "slides.pptx"):
            d["slides"] = url
        if url := self.get_url(project_name, "video.mp4"):
            d["video"] = url
        
        return d
        
    def projects_dict(self) -> dict:
        raise NotImplementedError
