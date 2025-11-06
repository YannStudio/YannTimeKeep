from utils.storage import *
from tkinter import ttk, messagebox, simpledialog
from models.session import *

def startNewSession():
    date = load_data()
    name = simpledialog.askstring("Nieuw project", "Projectnaam:")

    newSession = Session(name)
    newSession.show()

