import uuid

class Project:

    def __init__(self,projectName):
        
        self.projectId = uuid.uuid4()
        self.projectName = projectName
        self.projectSessions = []

    def show(self):
        print(f"ID + projectnaam: {self.projectId} / {self.projectName}")