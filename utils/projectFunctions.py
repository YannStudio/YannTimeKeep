from utils.storage import *
from tkinter import ttk, messagebox, simpledialog
from models.project import *

def addNewProject():
    data = load_data()
    name = simpledialog.askstring("Nieuw project", "Projectnaam:")

    newProject = Project(name)
    newProject.show()

    data[name] = newProject.parseToJson()
    save_data(data)

def loadProjects():
    data = load_data()
    projects = [Project.parseFromJson(p) for p in data.values()]

    for y in projects:
        print (y.projectId + "  -  " + y.projectName)
