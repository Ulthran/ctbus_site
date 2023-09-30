import requests


class Backend:
    def __init__(self) -> None:
        self.cdn_url = "d3047k2vzxu60t.cloudfront.net"

    def list_projects(self) -> list:
        raise NotImplementedError

    def url_exists(self, url):
        request = requests.head(url)
        if request.status_code == 200:
            return True
        else:
            return False

    def get_url(self, project: str, key: str) -> str:
        url = f"https://{self.cdn_url}/projects/{project}/{key}"
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
