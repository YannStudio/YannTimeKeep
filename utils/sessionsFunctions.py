from utils.storage import *
from tkinter import ttk, messagebox, simpledialog
from models.project import *

def startNewSession():
    date = load_data()
    name = simpledialog.askstring("Nieuw project", "Projectnaam:")

    newProject = Project(name)
    newProject.show()

