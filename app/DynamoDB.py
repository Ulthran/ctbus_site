import boto3
from collections import OrderedDict
from DB import DB

class DynamoDB(DB):
    def __init__(self, table_name: str) -> None:
        super().__init__()

        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        self.table = self.dynamodb.Table(self.table_name)
        self.projects = self.table.scan()["Items"]
        self.projects.sort(key = lambda x: x["rank"])

    def list_projects(self) -> list:
        return [o["project"] for o in self.projects]

    def project_dict(self, project_name: str) -> dict:
        d = super().project_dict(project_name)

        for project in self.projects:
            if project["project"] == project_name:
                d["title"] = project["title"]
                d["description"] = project["description"]
                d["tags"] = project["tags"]
                d["links"] = project["links"]
        
        print(d)
        return d
    
    def projects_dict(self) -> dict:
        d = OrderedDict()

        for i, project in enumerate(self.list_projects()):
            e = {}

            if url := self.get_url(project, "thumbnail.png"):
                e["thumbnail"] = url
            e["title"] = self.projects[i]["title"]
            e["description"] = self.projects[i]["description"]
            e["tags"] = self.projects[i]["tags"]
            e["links"] = self.projects[i]["links"]

            d[project] = e
        
        return d