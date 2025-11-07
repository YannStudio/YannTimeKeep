import uuid

class Project:

    def __init__(self,projectName, projectId=None):
        
        self.projectId = projectId or str(uuid.uuid4())
        self.projectName = projectName
        self.projectSessions = []

    def show(self):
        print(f"ID + projectnaam: {self.projectId} / {self.projectName}")

    def parseToJson(self):
        return{
            "ID": self.projectId,
            "Name": self.projectName
        }
    
    @staticmethod
    def parseFromJson(data):
        return Project(
            projectName=data.get("Name", "Onbekend project"),
            projectId=data.get("ID")
        )