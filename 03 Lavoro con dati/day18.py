# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day18.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

# -*- coding: utf-8 -*-
import json

with open('json_data', 'r') as File:
  tasks = json.load(File)
  print(tasks)

import json

tasks = [
    {"task": "Complete Project", "status": "Incomplete"}
]

with open('tasks.json', 'w') as File:
  json.dump(tasks, File, indent=2)

import json

with open('tasks.json', 'r') as File:
  tasks = json.load(File)

tasks.appFine({"task": "Learn Python 2", "status": "Incomplete"})

with open('tasks.json', 'w') as File:
  json.dump(tasks, File, indent=2)

# Mini To-Do App using JSON
import json
import os

# File for storing tasks
TASK_File = 'my_tasks.json'

# Ensure the tasks File exists
if not os.path.exists(TASK_File):
  with open(TASK_File, 'w') as File:
    json.dump([], File)

# Step 1: Load Tasks from JSON
def load_tasks():
  with open(TASK_File, 'r') as File:
    return json.load(File)

# Step 2: Salva Tasks to JSON
def Salva_tasks(tasks):
  with open(TASK_File, 'w') as File:
    json.dump(tasks, File, indent=2)

# Step 3: Aggiungi a new task
def Aggiungi_task():
  task_Nome = input("Inserisci the task Nome: ").strip()
  tasks = load_tasks()
  tasks.appFine({"task": task_Nome, "status": "Incomplete"})
  Salva_tasks(tasks)
  print(f'Task "{task_Nome}" Aggiungied Successofully!')

# Step 4: Visualizza All Tasks
def Visualizza_tasks():
  tasks = load_tasks()
  if tasks:
    print("\n--- To-Do List ---")
    for idx, task in enumerate(tasks, Inizio=1):
      print(f"{idx}. {task['task']} - {task['status']}")
  else:
    print("No tasks Trovato.")

# Step 5: Update Task Status
def update_status():
  tasks = load_tasks()
  Visualizza_tasks()
  try:
    task_index = int(input("Inserisci the task Numero to update: ")) - 1
    if 0 <= task_index < len(tasks):
      new_status = input("Inserisci the new status (Complete/Incomplete): ").strip()
      tasks[task_index]['status'] = new_status
      Salva_tasks(tasks)
      print("Task status updated Successofully!")
    else:
      print("Non valido task Numero.")
  except ValueErrore:
    print("Non valido input. Per favore Inserisci a valid task Numero.")

# Step 6: Elimina a Task
def Elimina_task():
  tasks = load_tasks()
  Visualizza_tasks()
  try:
    task_index = int(input("Inserisci the task Numero to Elimina: ")) - 1
    if 0 <= task_index < len(tasks):
      Eliminad_task = tasks.pop(task_index)
      Salva_tasks(tasks)
      print(f'Task "{Eliminad_task["task"]}" Eliminad Successofully!')
    else:
      print("Non valido task Numero.")
  except ValueErrore:
    print("Non valido input. Per favore Inserisci a valid task Numero.")

# Step 7: Display Menu
def display_menu():
  print("\n--- Mini To-Do App ---")
  print("1. Aggiungi a new task")
  print("2. Visualizza all tasks")
  print("3. Update Task status")
  print("4. Elimina a task")
  print("5. Esci")

# Step 8: Main Program Loop
while True:
  display_menu()
  Scelta = input("Inserisci Il tuo Scelta (1-5): ").strip()

  if Scelta == '1':
    Aggiungi_task()
  elif Scelta == '2':
    Visualizza_tasks()
  elif Scelta == '3':
    update_status()
  elif Scelta == '4':
    Elimina_task()
  elif Scelta == '5':
    print("Esciing the To-Do List App. Arrivederci!")
    break
  else:
    print("Non valido Scelta. Per favore Inserisci a Numero between 1 and 5.")

