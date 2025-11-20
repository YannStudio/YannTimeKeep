import json
import time
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkintertable import TableCanvas, TableModel
from utils.projectFunctions import *


#TKinter setup

root = tk.Tk()
root.title("Time Tracker")
root.geometry("600x400")
frameTop = tk.Frame(root)
frameTop.pack(fill="x", pady=10, padx=10)
frameTable = tk.Frame(root)
frameTable.pack(fill="x", pady=10, padx=10)

#Initiate table on startup
projects = []
projects = loadProjects()
tableData = parseProjectsToTableData(projects)

model = TableModel()
model.importDict(tableData)

table = TableCanvas(frameTable, model=model, editable=False)
table.show()

#TKinter functions

def refreshTable():
    global projects, model
    # Nieuwe data ophalen uit json
    projects = loadProjects()
    tableData = parseProjectsToTableData(projects)

    # Nieuwe model maken en in de table steken
    global model  # als je model elders nog gebruikt
    model = TableModel()
    model.importDict(tableData)

    table.updateModel(model)  # nieuw model koppelen
    table.redraw()            # tabel opnieuw tekenen

def editSelectedProject():
    global projects, model
    rowKey = table.getSelectedRow()
    if rowKey is None:
        messagebox.showwarning("Geen selectie gemaakt")
        return
    
    rowIndex =int(rowKey)
    record = model.getRecordAtRow(rowIndex)
    selectedProjectId = record.get("ID")
    selectedProjectName = record.get("Project naam")
    selectedProject = None
    for p in projects:
        if str(p.projectId) == str(selectedProjectId):
            selectedProject = p
            break
    if selectedProject is None:
        messagebox.showwarning("Geen project gevonden")
        return
    newProjectName = simpledialog.askstring(
        "Project bewerken",
        f"Nieuwe projectnaam:",
        initialvalue = selectedProjectName
    )
    
    if not newProjectName:
        return  
    
    selectedProject.projectName = newProjectName
    saveProjects(projects)
    refreshTable()
    

def handleNewProject():
    addNewProject()
    refreshTable()

#TKinter buttons and widgets

tk.Button(frameTop, text="Nieuw projecten", command=handleNewProject).pack(side="left", padx=5)
tk.Button(frameTop, text="Bewerken", command=editSelectedProject).pack(side="left", padx=5)

#Main loop

root.mainloop()

