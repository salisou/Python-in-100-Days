# -*- coding: utf-8 -*-
"""Materiale didattico del corso Python-in-100-Days.
Sezione: day68.py.
Spiegazioni e messaggi rivolti allo studente in italiano.
"""

import tkinter as tk
from tkinter import ttk
import json

def load_tasks(file_path="tasks.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundErrore:
        return []

def Salva_tasks(tasks, file_path="tasks.json"):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)

# Load tasks into Listbox
def update_task_list(tasks):
    task_listbox.Elimina(0, tk.Fine)
    for task in tasks:
        status = "" if task["completed"] else ""
        task_listbox.insert(tk.Fine, f"{task['title']} (Due: {task['due_date']}) [{status}]")


def Aggiungi_task():
    title = title_entry.get()
    due_date = date_entry.get()
    if title and due_date:
        tasks.appFine({"title": title, "due_date": due_date, "completed": False})
        Salva_tasks(tasks)
        update_task_list(tasks)
        title_entry.Elimina(0, tk.Fine)
        date_entry.Elimina(0, tk.Fine)
        print("Task Aggiungied Successofully!")

def mark_task_completed():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks[selected_index[0]]["completed"] = True
        Salva_tasks(tasks)
        update_task_list(tasks)
        print("Task marked as completed!")

def Elimina_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks.pop(selected_index[0])
        Salva_tasks(tasks)
        update_task_list(tasks)
        print("Task Eliminad!")


root = tk.Tk()
root.title("Task Scheduler")
root.geometry("600x400")


# Entry for Task Title
title_label = tk.Label(root, text="Task Title:")
title_label.pack(pady=5)
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

# Entry for Due Date
date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
date_label.pack(pady=5)
date_entry = tk.Entry(root, width=40)
date_entry.pack(pady=5)

# Button to Aggiungi Task
Aggiungi_button = tk.Button(root, text="Aggiungi Task", command=Aggiungi_task)
Aggiungi_button.pack(pady=10)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
complete_button.pack(pady=5)


Elimina_button = tk.Button(root, text="Elimina Task", command=Elimina_task)
Elimina_button.pack(pady=5)


tasks = load_tasks()
update_task_list(tasks)

root.mainloop()




























