class Session:
    def __init__(self,projectName):
        
        self.projectName = projectName

    def show(self):
        print(f"Projectnaam: {self.projectName}")