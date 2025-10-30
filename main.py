import json
import time
from datetime import datetime
from pathlib import Path
import tkinter as tk

#Functions to load an save data in json file

DATA_FILE = Path("data/sessions.json")

def load_data():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


#Functions to start, stop and review sessions in commandline program

def start_session(project_name):
    data = load_data()
    if project_name not in data:
        data[project_name] = []
    session = {"start": datetime.now().isoformat(), "end": None}
    data[project_name].append(session)
    save_data(data)
    print(f"Started session for {project_name} at {session['start']}")

def stop_session(project_name):
    data = load_data()
    if project_name not in data or not data[project_name]:
        print("No active session found.")
        return
    last = data[project_name][-1]
    if last["end"] is not None:
        print("Last session already stopped.")
        return
    last["end"] = datetime.now().isoformat()
    save_data(data)
    print(f"Stopped session for {project_name} at {last['end']}")

def show_report():
    data = load_data()
    for project, sessions in data.items():
        total_seconds = 0
        for s in sessions:
            if s["end"]:
                start = datetime.fromisoformat(s["start"])
                end = datetime.fromisoformat(s["end"])
                total_seconds += (end - start).total_seconds()
        hours = total_seconds / 3600
        print(f"{project}: {hours:.2f} uur totaal")

#Commandline programm

if __name__ == "__main__":
    print("1. Start sessie\n2. Stop sessie\n3. Rapport")
    choice = input("Kies: ")
    if choice == "1":
        project = input("Projectnaam: ")
        start_session(project)
    elif choice == "2":
        project = input("Projectnaam: ")
        stop_session(project)
    elif choice == "3":
        show_report()
