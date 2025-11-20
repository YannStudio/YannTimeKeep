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

def saveProjects(projects):
    data ={}
    for project in projects:
        # key mag zijn wat jij handig vindt: projectId, projectName, ...
        key = str(project.projectId)
        data[key] = project.parseToJson()

    save_data(data)

def loadProjects():
    data = load_data()
    projects = [Project.parseFromJson(p) for p in data.values()]
    return projects

def parseProjectsToTableData(projectList):
    tableData ={}

    for i, project in enumerate(projectList):
        rowKey = str(i)
        tableData[rowKey] = {
            "ID": project.projectId,
            "Project naam": project.projectName
        }

    return tableData