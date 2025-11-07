import json
import time
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkintertable import TableCanvas, TableModel
from utils.projectFunctions import *


#TKinter setup and widgets

root = tk.Tk()
root.title("Time Tracker")
root.geometry("600x400")
frameTop = tk.Frame(root)
frameTop.pack(fill="x", pady=10, padx=10)

tk.Button(frameTop, text="Nieuw projecten", command=addNewProject).pack(side="left", padx=5)
tk.Button(frameTop, text="Laad projecten", command=loadProjects).pack(side="left", padx=5)


#Main loop

root.mainloop()

